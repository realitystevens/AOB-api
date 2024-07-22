import random
import string
from django.db import models
from django.apps import apps
from django.utils.timezone import datetime
from cloudinary.models import CloudinaryField
from ckeditor_uploader.fields import RichTextUploadingField
from decouple import config




def productHash():
    return ''.join(random.choices(string.ascii_lowercase, k=5))


def tagHash():
    return ''.join(random.choices(string.digits, k=3))




class Tag(models.Model):

    name = models.CharField(
        max_length = 100,
        blank = False,
        default = '',
        help_text = 'Name of Tag'
    )

    id_hash = models.CharField(
        max_length = 3, 
        default = tagHash,
        primary_key = True,
        unique = True,
        help_text = 'Unique ID for the tag',
        blank = True,
    )



class Product(models.Model):

    name = models.CharField(
        max_length = 1000, 
        blank = True,
        default = '', 
        help_text = 'Name of Product'
    )

    description = models.TextField(
        blank = True,
        default = '',
        help_text = 'Description of Product (Displayed for Featured Products)'
    )

    tags = models.ManyToManyField(
        Tag,
    )

    if config('ENVIRONMENT') == 'PRODUCTION':
        image = CloudinaryField('image')
    else:
        image = models.ImageField(
            upload_to = 'assets/products', 
            blank = True, 
            default = ''
        )
    
    image_alt = models.CharField(
        max_length = 100,
        blank = True,
        default = ''
    )

    content = RichTextUploadingField()

    price = models.CharField(
        max_length = 100, 
        blank = True,
        default = '', 
    )

    url_hash = models.SlugField(
        max_length = 5, 
        default = productHash,
        primary_key = True,
        unique = True,
        help_text = 'Unique URL path for the Product',
        blank = True,
    )

    is_featured = models.BooleanField(
        default = False,
        blank = True,
    )

    is_published = models.BooleanField(
        default = False,
        blank = True,
    )

    created_at = models.DateTimeField(
        default = datetime.now,
        blank = True,
    )

    published_at = models.DateTimeField(
        default = datetime.now if is_published else None,
        editable = True,
        blank = True,
    )
        


    class Meta:
        ordering = ('name', 'url_hash', 'price', 'is_published', 'is_featured', 'created_at', 'published_at',)


    def __str__(self):
        return self.url_hash
