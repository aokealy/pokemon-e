from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):


    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
 

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    condition = None
    if 'product_condition' in request.POST:
        condition = request.POST['product_condition']
    cart = request.session.get('cart', {})

    if condition:
        if item_id in list(cart.keys()):
            if condition in cart[item_id]['items_by_condition'].keys():
                cart[item_id]['items_by_condition'][condition] += quantity
            else:
                cart[item_id]['items_by_condition'][condition] = quantity
        else:
            cart[item_id] = {'items_by_condition': {condition: quantity}}
    else:


     if item_id in list(cart.keys()):
        cart[item_id] += quantity
     else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)    
