from django.shortcuts import render, redirect, reverse
from django.http import Http404, JsonResponse
from django.shortcuts import HttpResponse, get_object_or_404
from product.models import Product, ProductImage
from django.contrib import messages

# Create your views here.
def show_order(request):
    """View for order page"""
    bag = request.session.get('bag', {})
    
    return render (request, 'order/order.html', bag)

def add_order(request, books_id):
    
    """Add individual book to cart"""
    
    books_id = str(books_id)
    product = get_object_or_404(Product, id=books_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    
    if books_id in list(bag.keys()):
        bag[books_id] += quantity
        messages.success(request, f'Added {product.name} quantity {quantity} to your bag')
    else:
        bag[books_id] = quantity
        messages.success(request, f'Added {product.name} quantity {quantity} to your bag')
    
    request.session['bag'] = bag

    return redirect (reverse('order'))


def adjust_order(request, item_id):
    """
    Adjust book quantity
    """
    item_id = str(item_id)
    product = get_object_or_404(Product, id=item_id)
    quantity = int(request.POST.get('quantity'))
    
    bag = request.session['bag']
    if request.method == "POST":
        if item_id in list(bag.keys()):
            bag[item_id] = quantity
            messages.success(request, f'Adjusted {product.name} quantity to {quantity}')
            if quantity == 0:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} from cart.')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Adjusted {product.name} quantity')
            return render (request, 'order/order.html')
    else: 
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('order'))


def remove_order(request, item_id):
    """Remove individual product from the cart"""
    item_id = str(item_id)
    
    try:
        
        product = get_object_or_404(Product, id=item_id)
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            quantity = 0
            if quantity == 0:
                bag.pop(item_id)
            
            
            messages.success(request, f'Removed {product} from your cart')
            
            return JsonResponse({'message': f'Removed {product} from your cart'})
            # return HttpResponse(status=200)
        # request.session['bag'] = bag
    except Http404 as e:
        messages.error(request, f'Error removing item: {e}')
        
        return HttpResponse(status=404)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        
        return HttpResponse(status=500)
    
    return redirect (reverse('order'))

def remove_all(request):
    
    bag = request.session.get('bag', {})
    bag.clear()
    request.session.modified = True
    request.session['bag'] = bag
    messages.success(request, f'Removed all books from your cart')

    return redirect (reverse('order'))