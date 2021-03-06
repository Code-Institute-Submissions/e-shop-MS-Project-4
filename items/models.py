from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=240, default='Give a name')
    introduction = models.TextField(default='some intro')
    features = models.CharField(max_length=240, default='some features')
    description = models.TextField()
    code = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    category_choices = (
        ('w', 'Women Clothes'),
        ('m', 'Men Clothes'),
        ('k', 'Kids Clothes'),
    )
    categories = models.CharField(max_length=15, choices=category_choices, default='w')
    availability = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

"""Connects the size with the Item in the Admin Panel"""
class Size(models.Model):
    sizes_choices = (
        ('s', 'Small'),
        ('m', 'Medium'),
        ('l', 'Large')
    )
    size = models.CharField(max_length=200, choices=sizes_choices)
    item = models.ManyToManyField(Item, related_name='sizes')
    
    def __str__(self):
        return self.size
