from django.urls import path
from PosApp import views

urlpatterns = [
    path('', views.index, name= 'index' ),
    path('home/', views.home, name= 'home' ),
    path('shelf/', views.shelf, name= 'shelf' ),
    path('edit_shelf/<str:pk>/', views.edit_shelf, name= 'edit_shelf' ),
    path('delete_shelf/<str:pk>/', views.delete_shelf, name= 'delete_shelf' ),
]