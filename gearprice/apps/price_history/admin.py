from django.contrib import admin
from gearprice.apps.price_history.models import Gear, Url, PriceHistory, Brand, GearType, Store, Alarm

class UrlInline(admin.TabularInline):
    model = Url

class GearAdmin(admin.ModelAdmin):
    inlines = [UrlInline]

# Register your models here.
admin.site.register(GearType)
admin.site.register(Brand)
admin.site.register(Alarm)
admin.site.register(Store)
admin.site.register(Gear, GearAdmin)
admin.site.register(Url)
admin.site.register(PriceHistory)
