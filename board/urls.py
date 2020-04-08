from django.urls import path

from .views import index, by_conf, ContCreateView

urlpatterns = [
               path('adds/', ContCreateView.as_view(), name='add'),
	path('<str:rubric_id>/', by_conf, name='by_conf'),
               path('', index, name='index'),
    ]
