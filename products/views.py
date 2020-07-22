import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from products.models import Product
from products.services import ProductService

product_service = ProductService()


@csrf_exempt  # todo fix this
def create_new_product(request):
    request_body = json.loads(request.body)
    product_to_create = Product(title=request_body['title'],
                                price=request_body['price'])
    created = product_service.create(product_to_create)
    return JsonResponse(model_to_dict(created), safe=False)


def get_all_products(request):
    all_products = product_service.get_all()
    return JsonResponse(
        [model_to_dict(product) for product in all_products],
        safe=False)
