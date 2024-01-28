from django.shortcuts import render, get_object_or_404
from .models import Profile, BookInterest
from .forms import ProfileForm, BookInterestForm
# Create your views here.

def show_profile(request):
    """Render user profile"""
    
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    order = profile.orders.all()
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
        "order": order, 
        'bookform': bookform,
    }
    return render(request, template, context)

def order_history(request):
    """Show order history"""
    
    template = "customer/order_history.html"
    context ={
        "form": form,
        "profile": profile,
        "order": order, 
        'bookform': bookform,
    }
    return render(request, template)
