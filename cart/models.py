from django.db import models
from django.conf import settings
from mamazon.models import Productt

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, null=True. blank=True, on_delete=models.CASCADE) # userの会計カートは一つ
    products = models.ManyToManyField() # カートの数は多くてもいい
    total = models.DecimalField(default=0.00, max_digit=9, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
