from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    featured_products = Product.objects.filter(is_featured=True)[:8]
    return render(request, 'main_app/home.html', {
        'featured_products': featured_products
    })

def about(request):
    return render(request, 'main_app/about.html')

def products(request):
    products_list = Product.objects.all()[:8]
    categories = Category.objects.all()
    return render(request, 'main_app/products.html', {
        'products': products_list,
        'categories': categories
    })

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products_list = Product.objects.filter(category=category)[:8]
    categories = Category.objects.all()
    return render(request, 'main_app/products.html', {
        'products': products_list,
        'categories': categories,
        'category': category
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'main_app/product_detail.html', {
        'product': product,
        'related_products': related_products
    })

def services(request):
    """Сторінка послуг"""
    return render(request, 'main_app/services.html')

def contact(request):
    """Сторінка контактів"""
    return render(request, 'main_app/contact.html')

def projects(request):
    """Сторінка проектів"""
    return render(request, 'main_app/projects.html')