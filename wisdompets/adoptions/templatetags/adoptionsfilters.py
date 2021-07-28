from django import template


register = template.Library()


@register.filter
def get_attr(obj, attr):
    """Gets `attr` on the given class object `obj`."""
    return getattr(obj, attr, None)


@register.filter
def split(value, delim=" "):
    """Split the `value` string on `delim`."""
    return value.split(delim)


