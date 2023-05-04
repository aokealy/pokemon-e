from django.shortcuts import render, redirect, reverse, HttpResponse

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

def adjust_cart(request, item_id):
 

    quantity = int(request.POST.get('quantity'))
    condition = None
    if 'product_condition' in request.POST:
        condition = request.POST['product_condition']
    cart = request.session.get('cart', {})

    if condition:
         if quantity > 0:
            cart[item_id]['items_by_condition'][condition] = quantity
         else:
            del cart[item_id]['items_by_condition'][condition]
            if not cart[item_id]['items_by_condition']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):

    try:
        condition = None
        if 'product_condition' in request.POST:
            condition = request.POST['product_condition']
        cart = request.session.get('cart', {})

        if condition:
            del cart[item_id]['items_by_condition'][condition]
            if not cart[item_id]['items_by_condition']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)    
       
   

       

