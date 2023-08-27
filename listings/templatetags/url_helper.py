'''
Solution to search results pagination
source: stackoverflow (linked in readme)

'''
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    '''
    Returns the URL-encoded querystring for the current page,
    updating the params with the key/value pairs passed to the tag.
    '''
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return query.urlencode()
