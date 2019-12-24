from django.shortcuts import render, redirect, reverse

# Code adapted from Code Institute

# View everything in cart

def view_cart(request):
    return render(request, "cart/cart.html")

# Add to cart


def add_to_cart(request, id):
    
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('index'))

# Adjust quantity against price

def adjust_cart(request, id):
    
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))