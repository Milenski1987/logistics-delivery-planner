from django import template

register = template.Library()

@register.filter(name='birth_date')
def birth_date(date):
    if not date:
        return ''
    return date.strftime("%d.%m.%Y")
