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
    
    bag = request.session.get('bag', {})
    # item = request.session.get('item', {})
    images = ProductImage.objects.all()

    for books_id, order_data in bag.items():
        print("books_id, order_data", books_id, order_data)
        if isinstance(order_data, int):
            product = get_object_or_404(Product, pk=books_id)
            print("product", product)
            print("price", product.price)
            print("quantity", order_data)
            total += order_data * product.price
            print("total", total)
            product_count += order_data
            existing_item = next((item for item in bag_items if item['product'].id == int(books_id)), None)
            print('existing_item', existing_item)
            if existing_item:
                print("Yes")
                # If the product is found, update its quantity
                existing_item['quantity'] += order_data
                for item in bag_items:
                    if item['product'].id == int(books_id):
                        item['quantity'] += order_data
                bag_items.append({
                    'books_id': books_id,
                    'quantity': order_data,
                    'product': product,
                    'total': total,
                })
            else:
                print('no')
                # Otherwise, add a new entry
                new_total = order_data * product.price
                print("new total", total)
                product_count = order_data
                print("product_count", product_count)
                bag_items.append({
                    'books_id': books_id,
                    'quantity': order_data,
                    'product': product,
                    'total': total,
                })

        delivery = total * settings.DELIVERY_PERCENTAGE/100
        print("delivery", delivery)
        overall_total = total + delivery
        print("overall_total", overall_total)
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