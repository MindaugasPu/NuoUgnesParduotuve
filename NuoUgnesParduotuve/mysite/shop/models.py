from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=150)
    price = models.IntegerField(_('Price'))
    description = models.TextField(_('Description'), null=True, blank=True)
    cover = models.ImageField(_('Cover'), upload_to='covers', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    CATEGORY_CHOICES = (
        ('1', _('Kita')),
        ('2', _('Auskarai')),
        ('3', _('Apyrankės')),
        ('4', _('Sagės')),
        ('5', _('Kaklo papuošalai')),
        ('6', _('Aksesuarai')),
        ('7', _('Dovanų kuponai')),
        ('8', _('Kalėdiniai vainikai')),
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    delivery = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=30, null=True, blank=True)

    ORDER_STATUS = (
        ('p', _('Pending')),
        ('a', _('Approved')),
        ('c', _('Cancelled')),
        ('d', _('Completed')),
    )

    status = models.CharField(
    max_length=1,
    choices=ORDER_STATUS,
    blank=True,
    default='p',
    help_text=_('Status'),
    )

    def __str__(self):
        return str(self.id)

    def total(self):
        sum_total = 0
        lines = self.lines.all()
        for line in lines:
            sum_total += line.sum()
        return sum_total

    def total_qty(self):
        total_qty = 0
        lines = self.lines.all()
        for line in lines:
            total_qty += line.quantity
        return total_qty


    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ['-id']

class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='lines')
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def sum(self):
        total = self.product.price * self.quantity
        return total

    class Meta:
        verbose_name = _('Order Line')
        verbose_name_plural = _('Order Lines')

    def __str__(self):
        return f"{self.product}, {self.order}, {self.quantity}"


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(_('Address'), max_length=150, null=True)
    city = models.CharField(_('City'), max_length=150, null=True)
    zip_code = models.CharField(_('Zip Code'), max_length=150, null=True)
    telephone = models.CharField(_('Telephone number'), max_length=20, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    country = models.CharField(_('Country'), max_length=30, null=True)

    def __str__(self):
        return f"{self.customer}, {self.order}, {self.address}"

    class Meta:
        verbose_name = _('ShippingAddress')
        verbose_name_plural = _('ShippingAddresses')