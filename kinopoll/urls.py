from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/<int:poll_id>/vote/', views.vote, name='vote'),
]