# -*- coding: utf-8 -*-

from django import template
from django.template.loader import render_to_string


register = template.Library()


@register.simple_tag(takes_context=True)
def cookielaw_banner(context):
    if context['request'].COOKIES.get('cookielaw_accepted', False):
        return ''
    return render_to_string('cookielaw/banner.html', dict(context))


@register.inclusion_tag('cookielaw/banner.html')
def cookielaw_banner_js_mode():
    return {'js_mode': True}
