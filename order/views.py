from django.shortcuts import render, redirect, reverse
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
    product = get_object_or_404(Product, id=books_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    
    if books_id in list(bag.keys()):
        bag[int(books_id)] += quantity
        messages.success(request, f'Added {product.name} quantity to your bag')
    else:
        bag[int(books_id)] = quantity
        messages.success(request, f'Added {product.name} quantity to your bag')
    item_items = bag.get('item_items')
    request.session['bag'] = bag
    

    
    context = {
        'order_items': request.session['bag']
    }

    return render (request, 'order/order.html', context)


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
            bag[item_id] += quantity
            messages.success(request, f'Adjusted {product.name} quantity to {quantity}')
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
    
    product = get_object_or_404(Product, id=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)
    messages.success(request, f'Removed {product.name} from your cart')
    request.session['bag'] = item
    return HttpResponse(status=200)


def remove_all(request):
    
    bag = request.session.get('bag', {})
    bag.clear()
    request.session.modified = True
    request.session['bag'] = bag
    messages.success(request, f'Removed all books from your cart')

    return redirect (reverse('order'))