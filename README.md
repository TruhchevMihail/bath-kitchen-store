# Bath & Kitchen Store

[![Django](https://img.shields.io/badge/Django-6.0.2-darkgreen?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-336791?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)](https://getbootstrap.com/)

A modern Django-based e-commerce platform for bathroom and kitchen products, built with modular architecture and clean development practices.

---

## Overview

Bath & Kitchen Store is a full-stack Django web application created for educational and examination purposes.  
It simulates a production-ready online store and demonstrates best practices in web development.

The project includes:

- Modular Django app structure
- Full CRUD implementation using Class-Based Views
- One-to-Many and Many-to-Many relationships
- Advanced filtering and search
- Reusable pagination system
- Session-based shopping cart
- PostgreSQL database integration
- Custom validation logic

---

## Features

### CRUD System
Complete Create, Read, Update and Delete functionality for:
- Products
- Brands
- Categories
- Project posts

Implemented using Django Class-Based Views and ModelForms.

### Search & Filtering
Users can:
- Search products by keyword
- Filter by category
- Filter by brand
- Navigate by section (Bath / Kitchen)

Search functionality is built using Django QuerySets and Q objects.

### Pagination
Product listings are paginated (e.g., 12 per page) to improve performance and usability.  
Pagination preserves active filters and search parameters.

### Shopping Cart
Session-based shopping cart that allows users to:
- Add products
- Update quantities
- Remove items
- View automatic total price calculation
- Access cart preview from navigation bar

No authentication is required.

### Many-to-Many Relationships
Projects are connected to multiple products.  
Each product can appear in multiple projects, enabling flexible content management.

---

## Architecture

The project is structured into multiple Django apps:

- **Catalog** – Manages products, categories and brands  
- **Projects** – Handles project posts with Many-to-Many product relations  
- **Shopping Cart** – Manages session-based cart logic  
- **Core** – Contains shared validators and utilities  

Each app follows separation of concerns and clean architecture principles.

---

## Database Structure

Relationships implemented:

- Brand → Product (One-to-Many)  
- Category → Product (One-to-Many)  
- ProjectPost ↔ Product (Many-to-Many)  

PostgreSQL is used as the database system.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/BathKitchenStore.git
cd BathKitchenStore
```

Create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
DB_NAME=bathkitchen_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
SECRET_KEY=your-secret-key
DEBUG=True
```

Apply migrations:

```bash
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open in browser:

http://127.0.0.1:8000

---

## Validation & Security

Custom validators enforce:

- Valid price ranges  
- Maximum image size (15MB)  
- Allowed formats (jpg, jpeg, png, webp)  

Sensitive configuration values are stored in environment variables.

---

## TODO (Future Improvements)

### E-commerce & Business Logic
- [ ] Add a real checkout flow (Order + OrderItem models) instead of “cart only”.
- [ ] Stock / inventory tracking (available quantity + “out of stock” UI).
- [ ] Discounts / promo codes (percentage or fixed amount).
- [ ] Shipping and billing details form (address, phone, delivery notes).
- [ ] “Save for later” / wishlist feature.

### Users & Permissions
- [ ] Add user authentication (register/login) and connect cart to a user profile (optional).
- [ ] Restrict create/edit/delete views to staff/admin only (if not already).
- [ ] Add a simple “My account” page (orders, saved items).

### Quality & Testing
- [ ] Add automated tests (models, forms, views, cart logic).
- [ ] Add basic linting/formatting (black/isort/flake8) and pre-commit hooks.
- [ ] Add CI pipeline (GitHub Actions) to run tests automatically.

### Performance & UX
- [ ] Add caching for heavy list pages (products/projects).
- [ ] Improve empty states (better messages + links back to categories).
- [ ] Add better image handling (thumbnails, default placeholders, responsive images).
- [ ] Add accessibility pass (labels, aria attributes, keyboard navigation).

### Production Readiness
- [ ] Add custom `500.html` error page.
- [ ] Remove `.env` from version control and add `.env.example`.
- [ ] Add Docker support (Dockerfile + docker-compose for PostgreSQL).
- [ ] Add deployment guide (Render/Railway/Heroku-style steps).

---

## Additional Documentation
For extended documentation and technical details, see:
- [Architecture & Technical Documentation](docs/ARCHITECTURE_AND_TECHNICAL_DOCUMENTATION.md)
- [User & Admin Guide](docs/USER_AND_ADMIN_GUIDE.md)
- [Developer Cheat Sheet](docs/DEVELOPER_CHEAT_SHEET.md)
