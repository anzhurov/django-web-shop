from django.db import models


class Product(models.Model):
    """Model for product in the shop catalog"""

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    price = models.FloatField()

    class Meta:
        db_table = 'product'
