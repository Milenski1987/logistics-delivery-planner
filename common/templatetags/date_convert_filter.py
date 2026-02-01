from django import template

register = template.Library()

@register.filter(name='date_convert')
def date_convert(date):
    if not date:
        return ''
    return date.strftime("%d.%m.%Y")
