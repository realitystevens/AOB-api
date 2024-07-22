from django.contrib import admin
from .models import Product, Tag



admin.site.site_header = 'AOB Digital Store Administration'

admin.site.site_title = 'AOB Digital Store'



class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'url_hash', 'price', 'is_published', 'is_featured', 'created_at', 'published_at',)

    list_filter = ('is_published', 'is_featured', 'created_at', 'published_at',)

    search_fields = ('name__icontains', 'content__icontains', 'published_at__icontains', 'price__icontains', 'tags__icontains', 'url_hash__icontains',)

admin.site.register(Product, ProductAdmin)



class TagAdmin(admin.ModelAdmin):

    list_display = ('name', 'id_hash',)

    search_fields = ('name__icontains', 'id_hash__icontains',)

admin.site.register(Tag, TagAdmin)
