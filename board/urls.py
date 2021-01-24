from django.contrib import admin
from django.urls import path


from .views import index, selectors

urlpatterns = [
    path('<str:lang>', index, name='index'),
    path('<str:lang>/<str:select>', selectors, name='select'),
    
]
