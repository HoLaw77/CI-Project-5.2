from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import ConfirmOrder
from .models import Order, OrderDetail
from order.contexts import order_contents
from product.models import Product
from customer.models import Profile
from customer.forms import ProfileForm
import stripe
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.

@require_POST
def cache_checkout_data(request):
    try:
        payintentid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        user_id = request.user.id if request.user.is_authenticated else 0

        stripe.PaymentIntent.modify(payintentid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save-info': request.POST.get('save_info'),
            'username': user_id,
        })

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your order cannot be processed right now. Please try again.')
        return HttpResponse(content=str(e), status=404)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    intent = None

    if request.method == "POST":
        bag = request.session.get('bag', {})
        form_data = {
        "full_name": request.POST["full_name"],  
        "email": request.POST["email"], 
        "phone_number": request.POST["phone_number"], 
        "address1": request.POST["address1"], 
        "address2": request.POST["address2"], 
        "postcode": request.POST["postcode"], 
        "country": request.POST["country"],
        }

        confirm_order = ConfirmOrder(form_data)
        if confirm_order.is_valid():
            order = confirm_order.save()
            
            for books_id, order_data in bag.items():
                try: 
                    product = Product.objects.get(id=books_id)
                    if isinstance(order_data, int):
                        order_detail = OrderDetail(
                            order=order,
                            product=product,
                            quantity= order_data,
                        )
                        order_detail.save()
                        
                except Product.DoesNotExist:
                    order.delete()
                    return redirect(reverse('show_order'))
            request.session["save-info"] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', 
            args=[order.order_number]))
        else:
            
            messages.error(request, "Error with the information provided, please check the form.")

            
    else:

        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "No book in your cart now.")
            return redirect(reverse('book'))

            
        order_in_cart = order_contents(request)
        total = order_in_cart['overall_total']
        stripe_total = round(total * 100) 
        stripe.api_key = stripe_secret_key
        try:
            intent = stripe.PaymentIntent.create(
                amount = stripe_total,
                currency = settings.STRIPE_CURRENCY,
            )

            

        except stripe.error.StripeError as e:
            
            messages.error(request, f"Error processing payment: {e}")
            return redirect(reverse('checkout'))


        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                confirm_order = ConfirmOrder(initial={
                    'full_name': profile.full_name,
                    'email': profile.user.email,
                    'phone_number': profile.phone_number,
                    'country': profile.country,
                    'postcode': profile.postcode,
                    'address1': profile.address1,
                    'address2': profile.address2,
                    
                })
            except Profile.DoesNotExist:
                confirm_order = ConfirmOrder()
        else:
            
            confirm_order = ConfirmOrder()


        if not stripe_public_key:
            messages.warning(request, 'You forget to set your stripe public key.')


    template = "checkout/checkout.html"
    context = {
        "confirm_order": confirm_order,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret if intent else None,
    }

    return render (request, template, context)


def checkout_success(request, order_number):
    """Handle request when checkout successfully"""

    save_info = request.session.get("save-info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            order.profile = profile
            order.save()

            if save_info:
                profile_data = {
                    "full_name": order.full_name,
                    "email": order.email,
                    "phone_number": order.phone_number,
                    "address1": order.address1,
                    "address2": order.address2,
                    "postcode": order.postcode,
                    "country": order.country,
                }
                confirm_order_form = ProfileForm(profile_data, instance=profile)
                if confirm_order_form.is_valid():
                    confirm_order_form.save()

        except Profile.DoesNotExist:
            messages.warning(request, "No user profile found.")
    else:
        messages.warning(request, "User is not authenticated.")

    messages.success(
        request,
        f'Order successfully processed. Order number is {order_number}. \
        A confirmation email will be sent to {order.email}'
    )

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_number': order_number
    }
    confirmation_email(order_number)
    
    return render(request, template, context)

def confirmation_email(order_number, request):
    """Send confirmation email for customer after payment"""
    try:
        order = get_object_or_404(Order, order_number=order_number)
        customer_email = order.email
        order_number = order_number
        overall_total = order.overall_total
        date = order.date
        link = "https://ci-project5-4ad812effe24.herokuapp.com/customer/order_history/" + order_number

        subject = f'Payment Confirmation: {order_number}'
        
        # Using render_to_string to render HTML content from a template
        html_message = render_to_string('email/email_confirmation.html', 
        {'order_number': order_number, 'overall_total': overall_total, 'date': date, 
        'link': link})
        
        # Stripping HTML tags to get the plain text version of the email
        plain_message = strip_tags(html_message)
        
        from_email = 'howanlaw707@gmail.com'
        recipient_list = [customer_email]
        
        send_mail(subject, plain_message, from_email, recipient_list, 
        fail_silently=False)
        

    except Exception as e:
        messages.warning(request, f"error, no email sent. {e}")
