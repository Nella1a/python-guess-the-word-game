from django.contrib import admin

# Register your models here.

from .models import SecretWords

admin.site.register(SecretWords)