from django.urls import path
from Products import views


urlpatterns = [
    path('', views.Products, name="Products"),
    path('AddProducts/', views.AddProducts, name="AddProducts"),
    path('DeleteProduct/<str:pk>/', views.DeleteProduct, name="DeleteProduct"),
    path('UpdateProduct/<str:pk>/', views.UpdateProduct, name="UpdateProduct"),    
    path('Category/', views.category, name="Category"),
    path('edit_category/<str:pk>/', views.edit_category, name="edit_category"),    
    path('delete_category/<str:pk>/', views.delete_category, name="delete_category"),    

]