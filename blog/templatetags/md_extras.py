from django.template.defaultfilters import stringfilter
from django import template

import markdown as md


@template.Library().filter()
@stringfilter
def markdown(value: str):
    """
        Example: <p>{{ post.body | markdown | safe }}</p>
    """
    # For the extensions used, see https://python-markdown.github.io/extensions/fenced_code_blocks/
    return md.markdown(value, extension=["markdown.extensions.fenced_code"])
