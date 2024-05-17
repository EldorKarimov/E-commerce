from django.db import models
from common.models import BaseModel, Media
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Category(BaseModel):
    name = models.CharField(_('name'), max_length=150)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

class Product(BaseModel):
    name = models.CharField(max_length=150, verbose_name=_("name"))
    price = models.FloatField(_('price'))
    short_description = models.TextField(_("short description"))
    description = models.TextField(_("description"))
    instraction = RichTextField(_("instraction"))
    quantity = models.IntegerField(_("quantity"))
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_stock = models.BooleanField(_('in stock'), default=True)
    brand = models.CharField(_("brand"), max_length=255)
    discount = models.IntegerField(_('discount'), help_text='in percentage')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

class ProductColor(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.product.id} {self.color.id}"

class ProductColor(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    value = models.CharField(max_length=255, verbose_name=_('value'))

    def __str__(self):
        return f"{self.product.id} {self.value}"
    
class ProductReview(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=255)
    review = models.TextField(_("review"))
    rank = models.IntegerField(_("rank"))
    email = models.EmailField(_("email"))
    

    def __str__(self):
        return f"Product: {self.product.id}|User: {self.user.id}"
    


class Wishlist(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlists")
    user = models.ForeignKey("account.User", on_delete=models.CASCADE, related_name="wishlists")

    def __str__(self):
        return f"Product: {self.product.id}|User: {self.user.id}"