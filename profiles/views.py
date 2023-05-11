from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has successfully updated!')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    
    }

    return render(request, template, context)

def order_history(request, order_code):
    order = get_object_or_404(Order, order_code=order_code)

    messages.info(request, (
        f'This is a past confirmation for order number {order_code}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_succeed.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

