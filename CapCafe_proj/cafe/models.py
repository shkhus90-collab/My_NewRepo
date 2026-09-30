from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    class Meta:
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name
class MenuItems(models,Model):
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True )
    price=models.DecimalField(max_digits=8, decimal_places=2)
    image=models.ImageField(upload_to='menu/',blank=True,null=True)
    is_available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_new_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES=(
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

        

    