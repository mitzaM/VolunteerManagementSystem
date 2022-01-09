from django.template import Library

register = Library()


@register.inclusion_tag('fields/_form_input_field.html')
def input_element(field):
    return {
        'field': field,
    }


@register.inclusion_tag('fields/_form_select_field.html')
def select_element(field):
    try:
        field_value = int(field.value())
    except (ValueError, TypeError):
        field_value = field.value()
    return {
        'field': field,
        'field_value': field_value,
    }
