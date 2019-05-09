from django.db import models

class CookieLawBanner(models.Model):
    banner_button = models.CharField(max_length=30)
    banner_text = models.TextField(max_length=200)
