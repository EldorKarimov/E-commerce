from django.contrib import admin
from .models import Category, Product, ProductColor, ProductReview, Wishlist

admin.site.register([Category, Product, ProductColor, ProductReview, Wishlist])
