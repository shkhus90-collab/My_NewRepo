
from django.contrib import admin
from django.urls import path	
from .views import issue_book, issue_confirmation, issue_success
urlpatterns = [
    path('issue/',issue_book, name='issue_book'),
    path('issue/confirm/',issue_confirmation, name='issue_confirmation'),
    path('issue/success/',issue_success, name='issue_success'),
    
]
