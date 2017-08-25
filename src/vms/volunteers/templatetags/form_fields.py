from django.template import Library

register = Library()


@register.inclusion_tag('fields/_form_input_field.html')
def input_element(field):
    return {
        'field': field,
    }
