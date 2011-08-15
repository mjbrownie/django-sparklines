from django import template
from django.utils import simplejson
from django.utils.safestring import mark_safe

register = template.Library()
from sparklines.util import get_object_date_count_list


from django.conf import settings

try:
    STATIC_URL = settings.STATIC_URL
except:
    STATIC_URL = settings.MEDIA_URL

def _queryset_sparkline(queryset,date_field,options={},*args,**kwargs):
    _queryset_sparkline.counter += 1
    sparkline_type = 'queryset'
    counter = _queryset_sparkline.counter
    module_name = queryset.model._meta.module_name
    options = mark_safe( simplejson.dumps(options) )
    sparkline_list =  get_object_date_count_list(queryset,
            date_field, *args, **kwargs)

    return locals()

_queryset_sparkline.counter = 0

@register.inclusion_tag('sparklines/sparkline.html')
def queryset_sparkline(queryset,date_field,
        options={'type':'bar'},
        start = None,
        end = None,
        step = 1,
        mode='weeks'):

    return _queryset_sparkline(queryset,date_field, options, start,
        end , step , mode)

@register.inclusion_tag('sparklines/sparkline.html')
def sparkline(sparkline_list,options = {'type':'bar'}):
    options = mark_safe( simplejson.dumps(options) )
    sparkline_type = 'list'
    sparkline.counter += 1
    counter = sparkline.counter
    return locals()

sparkline.counter = 0

@register.inclusion_tag('sparklines/sparklines_script_tag.html')
def sparklines_script_tag():
    return {'STATIC_URL':STATIC_URL}
