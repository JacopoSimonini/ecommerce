from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.models import Cart
from .models import Category

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'products/category_detail.html', context)


def view_cart(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = None
    context = {'cart': cart}
    return render(request, 'cart/view_cart.html', context)