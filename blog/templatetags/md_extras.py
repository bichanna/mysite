from django.template.defaultfilters import stringfilter
from django import template

import markdown

register = template.Library()

@register.filter(name="markdown")
@stringfilter
def md(value: str):
    """Example: <p>{{ post.body | markdown | safe }}</p>"""
    # For the extensions used, see https://python-markdown.github.io/extensions/fenced_code_blocks/
    # This does not need sanitation because only I write posts!
    return markdown.markdown(value, extensions=["markdown.extensions.fenced_code"])