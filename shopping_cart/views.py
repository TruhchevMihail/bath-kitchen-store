from django.shortcuts import render

def cart_view(request):
    # TODO: connect to real cart logic with payment wall later
    return render(request, 'shopping_cart/cart.html')
