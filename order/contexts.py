from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from product.models import Product, ProductImage

def order_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    overall_total = 0
    delivery = 0
    new_total= 0    
    bag = request.session.get('bag', {})

    images = ProductImage.objects.all()

    for books_id, order_data in bag.items():
        print("books_id, order_data", books_id, order_data)
        if isinstance(order_data, int):
            product = get_object_or_404(Product, pk=int(books_id))
            total += order_data * product.price
            
            product_count += order_data
            existing_item = next((item for item in bag_items if item['product'].id == int(books_id)), None)
            
            if existing_item:
                print("existing_item is True")
                # If the product is found, update its quantity
                existing_item['quantity'] = order_data
                for item in bag_items:
                    print(f'item {item}')
                    if item['product'].id == int(books_id):
                        item['quantity'] += order_data
                bag_items.append({
                    'books_id': int(books_id),
                    'quantity': order_data,
                    'product': product,
                    'total': total,
                })
                print(f'appending {books_id} with quantity {order_data} (in if clause)')
            else:
                
                # Otherwise, add a new entry
                new_total += order_data * product.price
                
                product_count = order_data
        
                bag_items.append({
                    'books_id': int(books_id),
                    'quantity': order_data,
                    'product': product,
                    'total': total,
                    'new_total': new_total
                })
                print(f'appending {books_id} with quantity {order_data} (in else clause)')

        delivery = total * settings.DELIVERY_PERCENTAGE/100
        
        overall_total = total + delivery
        
    context = {
        "item_items": bag_items,
        "total": total,
        "product_count": product_count,
        "images": images,
        "overall_total": overall_total,
        "delivery": delivery
    }
    print("!!!!!!!!!!!!context", context)

    return context