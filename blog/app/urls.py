from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='article-list-all'),
    path('article/<str:slug>/', index, name='article-list')
]
