from django.template.defaultfilters import stringfilter
from django import template

import markdown

register = template.Library()

@register.filter(name="markdown")
@stringfilter
def md(value: str):
    """Example: <p>{{ post.body | markdown | safe }}</p>"""
    return markdown.markdown(value, extensions=["markdown.extensions.fenced_code"])