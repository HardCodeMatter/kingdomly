from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('country/', views.country_list, name='country_list'),
    path('country/<int:id>/', views.country_detail, name='country_detail'),
    path('country/<int:id>/edit/', views.country_edit, name='country_edit'),
    path('country/create/', views.country_create, name='country_create'),

    path('continent/', views.continent_list, name='continent_list'),
    path('continent/<int:id>/', views.continent_detail, name='continent_detail'),
]
