
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('issue/', views.issue_book_view, name='issue_book'),
    path('issue/confirm/', views.issue_confirmation_view, name='issue_confirmation'),
    path('issue/success/', views.issue_success_view, name='issue_success'),
    
]
