from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart currently")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    order_form = OrderForm()
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MzNKpBmLoLbFeg9Wc00RkY2okfX1armtPbUn6mVCEo7aJPcC0CaHfso2VfPcLTbMyQbHc8xGRAtkSWxnFhPmSjj00EGk8pp05',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
