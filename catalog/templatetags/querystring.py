from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def qs_no_page(context):
    
    request = context['request']
    qd = request.GET.copy()
    qd.pop('page', None)
    return qd.urlencode(qd, doseq=True)