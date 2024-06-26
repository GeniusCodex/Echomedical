from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return f'{self.title} - {self.slug}'
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='img')
    product_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username

    @property 
    def grandtotal(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.subtotal for item in cartitems])
        return total
    
    @property 
    def cartquantity(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total



class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
    
    @property
    def subtotal(self):
        total = self.quantity * self.product.price
        return total
    

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)