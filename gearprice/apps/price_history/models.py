from django.db import models
from django.utils.translation import ugettext_lazy as _


class GearType(models.Model):
    name = models.CharField(max_length=100)

    class meta:
        verbose_name = _('gear_type')
        verbose_name_plural = _('gear_types')

    def __unicode__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    class meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

    def __unicode__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100)
    xpath = models.CharField(max_length=500)

    class meta:
        verbose_name = _('store')
        verbose_name_plural = _('stores')

    def __unicode__(self):
        return self.name


class Gear(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, null=True)
    gear_type = models.ForeignKey(GearType, null=True)
    image_url = models.CharField(max_length=200, null=True)

    class meta:
        verbose_name = _('gear')
        verbose_name_plural = _('gears')

    def __unicode__(self):
        return self.name


class Alarm(models.Model):
    email = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    gear = models.ForeignKey(Gear, null=True)


class Url(models.Model):
    url = models.CharField(max_length=500)

    store = models.ForeignKey(Store, null=True)
    gear = models.ForeignKey(Gear)

    class meta:
        verbose_name = _('url')
        verbose_name_plural = _('urls')

    def __unicode__(self):
        return self.url


class PriceHistory(models.Model):
    date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    store_name = models.CharField(max_length=100, blank=True, null=True)

    gear = models.ForeignKey(Gear)

    class meta:
        verbose_name = _('price_history')
        verbose_name_plural = _('price_history')

    def __unicode__(self):
        return "PriceHistory: { 'store_name': %s, 'date': %s, 'price': %s }" % (self.store_name, self.date, self.price)
