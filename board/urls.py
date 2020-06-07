from django.urls import path

from .views import index, about

urlpatterns = [
               path('<str:lang>/<str:conf>', about, name='about'),
	path('<str:lang>/', index, name='index'),
    ]
