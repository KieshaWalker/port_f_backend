from django.urls import path
from . import views

urlpatterns = [
    # API endpoints for Next.js frontend
    path('profile/', views.api_profile, name='api_profile'),
    path('skills/', views.api_skills, name='api_skills'),
    path('projects/', views.api_projects, name='api_projects'),
    path('homepage/', views.api_homepage, name='api_homepage'),
]