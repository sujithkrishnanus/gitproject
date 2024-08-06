from django.contrib.auth.models import User
from django.db import models
from bookapp.models import Book


# Create your models here.

class cartModel(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Book)

class cartItem(models.Model):

    cart=models.ForeignKey(cartModel,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
