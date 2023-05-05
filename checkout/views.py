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

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
   
    
    

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        
       
    }

    return render(request, template, context)
