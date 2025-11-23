from django.urls import path
from .views import Index_views, Contact_views, Delete_views, Edit_views



urlpatterns = [
    path('', Index_views, name='index'),
    path('contact/', Contact_views, name='contact'),
    path('delete/<int:id>/', Delete_views, name='delete'),
    path('edit/<int:id>/', Edit_views, name='edit')
]
