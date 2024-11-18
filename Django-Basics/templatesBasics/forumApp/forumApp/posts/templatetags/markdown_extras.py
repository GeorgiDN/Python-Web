# pip install markdown

import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="markdown")
def markdown_format(text, my_param):
    print("My param is ", my_param)
    return mark_safe(markdown.markdown(text))
