from django.core import urlresolvers
from django.template import Library

register = Library()


@register.simple_tag(takes_context=True)
def active_class(context, url_names, return_value='active', **kwargs):
    try:
        resolved = urlresolvers.resolve(context.get('request').path)
    except:
        return ""

    for url_name in url_names.split():
        if resolved and url_name in resolved.view_name:
            return return_value
    return ""
