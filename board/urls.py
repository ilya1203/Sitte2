from django.urls import path

from .views import index

urlpatterns = [
	path('<str:lang>/<str:conf>/', index, name='index'),
    ]
