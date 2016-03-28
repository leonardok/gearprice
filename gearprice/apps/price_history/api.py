from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from gearprice.apps.price_history.models import Gear, Brand, GearType, Alarm


class MultipartResource(object):
    def deserialize(self, request, data, format=None):
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart'):
            data = request.POST.copy()
            data.update(request.FILES)
            return data

        return super(MultipartResource, self).deserialize(request, data, format)

    def put_detail(self, request, **kwargs):
        if request.META.get('CONTENT_TYPE').startswith('multipart') and \
                not hasattr(request, '_body'):
            request._body = ''

        return super(MultipartResource, self).put_detail(request, **kwargs)


class BrandResource(ModelResource):
    class Meta:
        queryset = Brand.objects.all()
        allowed_methods = ['get']
        resource_name = 'brand'


class AlarmResource(MultipartResource, ModelResource):
    class Meta:
        queryset = Alarm.objects.all()

        allowed_methods = ['post']
        resource_name = 'alarm'


class GearTypeResource(ModelResource):
    class Meta:
        queryset = GearType.objects.all()

        allowed_methods = ['get']
        resource_name = 'gear_type'

        filtering = {
            'name': ALL
        }


class GearResource(ModelResource):
    brand = fields.ToOneField(BrandResource, 'brand', full=False)
    gear_type = fields.ToOneField(GearTypeResource, 'gear_type', full=False)

    class Meta:
        queryset = Gear.objects.order_by('name')
        resource_name = 'gear'

        allowed_methods = ['get']

        filtering = {
            "brand": ALL_WITH_RELATIONS,
            "gear_type": ALL_WITH_RELATIONS,
        }

        fields = ['name', 'id']





