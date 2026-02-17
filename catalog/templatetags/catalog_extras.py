from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        return f'{float(value):.2f} EUR'
    except (TypeError, ValueError):
        return value

@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            d[k] = v
        else:
            d.pop(k, None)
    return d.urlencode()