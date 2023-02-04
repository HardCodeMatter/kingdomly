from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('country/', views.country_list, name='country_list'),
    path('country/<int:id>/', views.country_detail, name='country_detail'),
    path('country/<int:id>/edit/', views.country_edit, name='country_edit'),
    path('country/create/', views.country_create, name='country_create'),
]
