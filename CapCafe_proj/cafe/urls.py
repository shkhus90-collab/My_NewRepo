from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu_list_view, name='menu_list'),
    path('menu/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu_detail'),
    path('menu/add/', views.MenuItemCreateView.as_view(), name='menu_add'),
    path('menu/<int:pk>/edit/', views.MenuItemUpdateView.as_view(), name='menu_edit'),
    path('menu/<int:pk>/delete/', views.MenuItemDeleteView.as_view(), name='menu_delete'),
    path('dashboard/', views.staff_dashboard_view, name='staff_dashboard'),
]