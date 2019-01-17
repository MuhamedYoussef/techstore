from django.db import models
from datetime import datetime
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    details = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True)
    image_url = models.CharField(max_length=200, blank=True)
    best = models.BooleanField(default=False)
    added = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def summary(self):
        return self.details[:60]
