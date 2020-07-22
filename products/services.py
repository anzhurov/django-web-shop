from typing import List

from products.models import Product


class ProductService:
    def create(self, product: Product) -> Product:
        product.save()
        return product

    def get_all(self) -> List[Product]:
        return list(Product.objects.all())
