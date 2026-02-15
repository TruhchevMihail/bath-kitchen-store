from decimal import Decimal

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from catalog.models import Product


CART_SESSION_KEY = "cart"
MAX_QTY_PER_ITEM = 100


def _get_cart(session) -> dict:
    cart = session.get(CART_SESSION_KEY)
    if cart is None:
        cart = {}
        session[CART_SESSION_KEY] = cart
    return cart


def _save_session(session):
    session.modified = True


class CartView(TemplateView):
    template_name = "shopping_cart/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = _get_cart(self.request.session)

        product_ids = [int(pid) for pid in cart.keys()] if cart else []
        products_map = {p.id: p for p in Product.objects.filter(id__in=product_ids)}

        items = []
        total = Decimal("0.00")

        for pid_str, entry in cart.items():
            pid = int(pid_str)
            product = products_map.get(pid)
            if not product:
                continue
            qty = max(1, min(int(entry.get("qty", 1)), MAX_QTY_PER_ITEM))
            price = Decimal(product.price)
            subtotal = price * qty
            total += subtotal
            items.append({
                "product": product,
                "qty": qty,
                "price": price,
                "subtotal": subtotal,
            })

        context.update({
            "items": items,
            "total": total,
        })
        return context


class AddToCartView(View):
    def post(self, request: HttpRequest, slug: str):
        product = get_object_or_404(Product, slug=slug)

        try:
            qty = int(request.POST.get("qty", 1))
        except (TypeError, ValueError):
            qty = 1
        qty = max(1, min(qty, MAX_QTY_PER_ITEM))

        cart = _get_cart(request.session)
        key = str(product.id)
        current = int(cart.get(key, {}).get("qty", 0))
        new_qty = max(1, min(current + qty, MAX_QTY_PER_ITEM))

        cart[key] = {"qty": new_qty}
        _save_session(request.session)

        messages.success(request, f"Added {qty} × '{product.title}' to cart.")

        next_url = request.POST.get("next")
        return redirect(next_url or reverse("cart"))


class RemoveFromCartView(View):
    def post(self, request: HttpRequest, product_id: int):
        cart = _get_cart(request.session)
        key = str(product_id)
        if key in cart:
            cart.pop(key)
            _save_session(request.session)
            messages.info(request, "Item removed from cart.")
        return redirect("cart")


class UpdateCartView(View):
    def post(self, request: HttpRequest):
        cart = _get_cart(request.session)

        updated = 0
        for name, value in request.POST.items():
            if not name.startswith("qty-"):
                continue
            try:
                pid = int(name.split("-", 1)[1])
                qty = int(value)
            except (ValueError, IndexError):
                continue
            qty = max(0, min(qty, MAX_QTY_PER_ITEM))

            key = str(pid)
            if qty <= 0:
                if key in cart:
                    cart.pop(key)
                    updated += 1
            else:
                cart[key] = {"qty": qty}
                updated += 1

        if updated:
            _save_session(request.session)
            messages.success(request, "Cart updated.")

        return redirect("cart")


class ClearCartView(View):
    def post(self, request: HttpRequest):
        request.session[CART_SESSION_KEY] = {}
        _save_session(request.session)
        messages.info(request, "Cart cleared.")
        return redirect("cart")


class CheckoutView(TemplateView):
    template_name = "shopping_cart/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = _get_cart(self.request.session)

        product_ids = [int(pid) for pid in cart.keys()] if cart else []
        products_map = {p.id: p for p in Product.objects.filter(id__in=product_ids)}

        items = []
        total = Decimal("0.00")

        for pid_str, entry in cart.items():
            pid = int(pid_str)
            product = products_map.get(pid)
            if not product:
                continue
            qty = max(1, min(int(entry.get("qty", 1)), MAX_QTY_PER_ITEM))
            price = Decimal(product.price)
            subtotal = price * qty
            total += subtotal
            items.append({
                "product": product,
                "qty": qty,
                "price": price,
                "subtotal": subtotal,
            })

        context.update({"items": items, "total": total, "success": False})
        return context

    def post(self, request: HttpRequest):
        # session-based checkout: clear the cart and show success
        cart = _get_cart(request.session)

        product_ids = [int(pid) for pid in cart.keys()] if cart else []
        products_map = {p.id: p for p in Product.objects.filter(id__in=product_ids)}

        items = []
        total = Decimal("0.00")

        for pid_str, entry in cart.items():
            pid = int(pid_str)
            product = products_map.get(pid)
            if not product:
                continue
            qty = max(1, min(int(entry.get("qty", 1)), MAX_QTY_PER_ITEM))
            price = Decimal(product.price)
            subtotal = price * qty
            total += subtotal
            items.append({
                "product": product,
                "qty": qty,
                "price": price,
                "subtotal": subtotal,
            })

        request.session[CART_SESSION_KEY] = {}
        _save_session(request.session)
        messages.success(request, "Checkout completed. Your cart has been cleared.")
        return render(request, self.template_name, {"items": items, "total": total, "success": True})
