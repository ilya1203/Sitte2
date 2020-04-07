from django.urls import path

from .views import index, by_conf

urlpatterns = [
	path('<str:rubric_id>/', by_conf, name='by_conf'),
    path('', index, name='index'),
    ]
