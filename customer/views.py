from django.shortcuts import render, get_object_or_404
from .models import Profile, BookInterest
from .forms import ProfileForm, BookInterestForm
from checkout.models import Order, OrderDetail
from django.contrib import messages
# Create your views here.

def show_profile(request):
    """Render user profile"""
    
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    orders = profile.orders.all()
    try:
        # Try to get BookInterest for the profile
        bookinterest = BookInterest.objects.get(profile=profile)
        bookform = BookInterestForm(instance=bookinterest)
        
    except BookInterest.DoesNotExist:
        # If BookInterest does not exist, create a new one
        bookinterest = None
        bookform = BookInterestForm()


    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        form.save()
        bookform = BookInterestForm(request.POST, instance=bookinterest)
        bookform.save()

    
    template = "customer/customer.html"
    context ={
        "form": form,
        "profile": profile,
        "orders": orders, 
        'bookform': bookform,
    }
    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, f"This is your previous order {order_number}. A confirmation email was sent on the order date.")

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)
