from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from profiles.models import UserProfile

class Bag(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    total_price = models.DecimalField(
        max_digits = 10, decimal_places = 2, blank = True, null = True
)


    def save(self, *args, **kwargs):
        if self.product.price is not None and self.quantity is not None:
            self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.quantity} x {self.product.name} in bag" 