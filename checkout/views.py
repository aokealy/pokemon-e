from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart currently")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MzNKpBmLoLbFeg9Wc00RkY2okfX1armtPbUn6mVCEo7aJPcC0CaHfso2VfPcLTbMyQbHc8xGRAtkSWxnFhPmSjj00EGk8pp05',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
