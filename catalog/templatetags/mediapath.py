from django import template

register = template.Library()


@register.simple_tag
@register.filter()
def mediapath(data) -> str:
    return data.url if data else '#'
