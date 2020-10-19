from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

User = get_user_model()

class Address(models.Model):
    """
    Model to store multiple addresses for a customer/user.
    """

    address = models.TextField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=timezone.now)
    update_date = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return str(f'{self.address} - {self.customer}')


class Category(models.Model):
    """
    Model to create Categories for product.
    """

    name = models.CharField(max_length=250)

    def __str__(self):
        return str(f'{self.name}')


class Distributor(models.Model):
    """
    Moode to save the distributor of the product.
    """

    name = models.CharField(max_length=250)
    address = models.TextField(null=True, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=timezone.now)
    update_date = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return str(f'{self.name}')

class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return str(f'{self.name}')

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    Category = models.ManyToManyField(Category)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    creation_date = models.DateTimeField(auto_now_add=timezone.now)
    update_date = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.price}'


class OrderStatus(models.Model):
    status = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.status}'



class PaymentType(models.Model):
    payment_type = models.CharField(max_length=250)

class Order(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(auto_now_add=timezone.now)
    update_date = models.DateTimeField(auto_now=timezone.now)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(f'{self.creation_date} - {self.customer.first_name} - {self.order_status}')



class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.customer.first_name} - {self.product.name}')