from django.shortcuts import render


from django.shortcuts import render
from .models import Product, CartItem, Cart, Order


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








