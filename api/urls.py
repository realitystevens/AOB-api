from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product'),
]
