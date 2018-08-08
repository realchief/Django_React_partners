import re

from django import template

from social_django.utils import Storage

register = template.Library()

name_re = re.compile(r'([^O])Auth')


@register.filter
def icon_name(name):
    return {
        'google-oauth': 'google',
        'google-oauth2': 'google',
    }.get(name, name)


@register.simple_tag(takes_context=True)
def associated(context, backend):
    user = context.get('user')
    context['association'] = None
    if user and user.is_authenticated():
        context['association'] = Storage.user.get_social_auth_for_user(
            user,
            backend.name
        ).first()
    return ''
