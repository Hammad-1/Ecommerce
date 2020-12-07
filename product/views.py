
from django.shortcuts import render
from .models import Product, CartItem, Cart, Order
from .forms import Detail


def get_cart(request):

    cart_id = request.session.get('cart_id')
    if cart_id is None:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
        return cart
    else:
        return Cart.objects.get(id=cart_id)


def product(request):

    product = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('id')
        cartitem = CartItem.objects.create(
            cart=get_cart(request),
            product=Product.objects.get(id=product_id)
        )
        cartitem.save()

    return render(request, 'product/product.html', {'products': product})


def show_cart(request):
    cart_id = request.session.get('cart_id')
    cart_items = CartItem.objects.filter(cart=cart_id)
    return render(request, 'display_cart.html', {'cart_item': cart_items})


def checkout(request):
    cart_id = request.session.get('cart_id')
    cart_items = CartItem.objects.filter(cart=cart_id)
    if request.method == 'POST':
        form = Detail(request.POST)
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        postal_code = request.POST['postal_code']
        details = Order(
            cart_id=cart_id, name=name, phone_number=phone_number, email=email, address=address, postal_code=postal_code)
        details.save()
        return render(request, 'product/invoice.html')

    else:
        form = Detail()
        total = int()
        for price in cart_items:
            total += price.product.price

        return render(request, 'product/checkout.html', {'form': form, 'items': cart_items, 'total': total})


def invoive(request):
    cart_id = request.session.get('cart_id')
    cart_items = CartItem.objects.filter(cart=cart_id)
    total = int()
    for price in cart_items:
        total += price.product.price
    return render(request, 'product/invoice.html', {'cart_item': cart_items,
                                                    'total':total})







