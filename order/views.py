from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from product.models import Product, ProductImage


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
    else:
        bag[int(books_id)] = quantity
    item_items = bag.get('item_items')
    request.session['bag'] = bag
    

    # return render (request, "order/order.html")
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
        else:
            bag[item_id] = quantity
            # messages.success(request, f'Adjusted {product.name} quantity')
            return render (request, 'order/order.html')
    else: 
        bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(reverse('order'))


def remove_order(request, item_id):
    """Remove individual product from the cart"""
    product = get_object_or_404(Product, id=item_id)

    request.session['bag'] = {}
    # item = request.session.get('item', {})
    # item.pop(item_id)
    # messages.success(request, f'Removed {product.name} from your cart')

    # request.session['item'] = item
    return HttpResponse(status=200)


def remove_all(request):
    # request.session['bag'] = bag
    bag = request.session.get('bag', {})
    bag.clear()
    request.session.modified = True
    request.session['bag'] = bag

    return render (request, 'order/order.html')