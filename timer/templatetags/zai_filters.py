from urllib.parse import unquote
from django import template

register = template.Library()

@register.filter(name='urldecode')
def urldecode(value):
    return unquote(value)