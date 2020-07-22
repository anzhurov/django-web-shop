from django.db import models


class Product(models.Model):
    """Model for product in the shop catalog"""

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f'{self.id} - {self.title} - {self.price}$'

    class Meta:
        db_table = 'product'
