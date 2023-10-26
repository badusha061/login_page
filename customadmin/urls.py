from django.urls import path
from . import views

app_name = 'customadmin'

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),
    path('add/', views.add_views, name='add'),
    path('edit/', views.edit_views, name='edit'),
    path('update/<int:id>/', views.update_views, name='update'),
    path('delete/<str:id>', views.delete_views, name='delete'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('logout/', views.logout_view, name='logout'),
  
]
