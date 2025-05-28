from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_member, name='register'),
    path('success/<int:member_id>/', views.registration_success,
         name='registration_success'),
    path('membership/pending/', views.pending_members, name='pending_members'),
    path('approve/<int:member_id>/', views.approve_member, name='approve_member'),
    path('approved-members/', views.approved_members, name='approved_members'),
    path('reject/<int:member_id>/', views.reject_member, name='reject_member'),
]
