from django.contrib import admin
from .models import CookieLawBanner

class CookieLawBannerAdmin(admin.ModelAdmin):
    pass
admin.site.register(CookieLawBanner, CookieLawBannerAdmin)
