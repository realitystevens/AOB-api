from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token


admin.site.register(Token, TokenAdmin)
