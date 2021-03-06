# -*- coding: utf-8 -*-

from django import template
from django.template.loader import render_to_string

from cookielaw.models import CookieLawBanner

register = template.Library()


@register.simple_tag(takes_context=True)
def cookielaw_banner(context):
    if context['request'].COOKIES.get('cookielaw_accepted', False):
        return ''
    # Stop use fucked up context value
    context = {}
    context['cookielawbanner'] = CookieLawBanner.objects.first()
    try:
        return render_to_string('cookielaw/banner.html', context)
    except TypeError:
        # from django 1.11 context needs to be a dictionary
        return render_to_string('cookielaw/banner.html', context.__dict__)
