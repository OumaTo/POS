from django.urls import path
from Orders import views

urlpatterns = [
    path('', views.Orders, name='Orders'),
    path('CreateOrder/', views.NewOrder, name='CreateOrder'),
    path('Checkout/', views.Checkout, name='Checkout'),
    path('DeleteOrder/<str:pk>/', views.DeleteOrder, name='DeleteOrder'),
    path('Complete/<str:pk>/', views.Complete, name='Complete'),
    path('Cancel/<str:pk>/', views.Cancel, name='Cancel'),

]