from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents




def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart currently")
        return redirect(reverse('products'))

    
    
    

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MzNKpBmLoLbFeg9WvOlyYyrMcfTxJTzI9JYSuhtUpbZDgPyPbNoZoVekVRk1nFqvOe7SKgKqtuZ56LikeA4HZ6u006w6r6kRB',
        'client_secret': 'test client secret',
        
       
    }

    return render(request, template, context)
