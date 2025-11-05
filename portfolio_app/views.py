from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from .models import Profile, Project
import json

# API Endpoints for Next.js frontend

@require_GET
def api_profile(request):
    """API endpoint to get profile data"""
    try:
        profile = Profile.objects.first()
        if profile:
            data = {
                'name': profile.name,
                'bio': profile.bio,
                'email': profile.email,
                'profile_image': profile.profile_image.url if profile.profile_image else None,
            }
            print(f"Profile data: {data}")
        else:
            data = {
                'name': 'Kiesha Walker',
                'bio': 'Software Engineer | Full Stack Developer',
                'email': 'your.email@example.com',
                'profile_image': None,
            }
        return JsonResponse(data)
    except Exception as e:
        print(f"Error in api_profile: {e}")
        return JsonResponse({'error': str(e)}, status=500)
    print(f"Error in api_profile: {e}")
@require_GET
def api_skills(request):
    """API endpoint to get skills data"""
    skills = {
        'Frontend Development': ['React', 'Angular', 'SwiftUI', 'TypeScript', 'JavaScript (ES6+)', 'HTML5', 'CSS3', 'Material-UI', 'Bootstrap'],
        'Backend Development': ['Node.js', 'Express.js', 'Django', 'Flask', 'FastAPI', 'REST APIs', 'JWT Authentication', 'MongoDB', 'PostgreSQL', 'GraphQL'],
        'Programming Languages': ['Python', 'C++', 'Swift', 'Kotlin', 'JavaScript', 'TypeScript'],
        'Development Tools & DevOps': ['Git', 'Docker', 'Vite', 'Babel', 'Heroku', 'Netlify', 'Vercel', 'ESLint', 'Prettier', 'CI/CD Pipelines'],
        'Professional Skills': ['American Sign Language', 'Spanish', 'Multilingual Collaboration', 'Technical Leadership', 'Analytical Debugging', 'Self-Directed Learning'],
    }
    return JsonResponse(skills)

@require_GET
def api_projects(request):
    """API endpoint to get projects data"""
    try:
        projects = Project.objects.all().order_by('-created_at')
        projects_data = []
        for project in projects:
            project_data = {
                'id': project.id,
                'name': project.name,
                'description': project.description,
                'technologies': project.get_technologies_list(),
                'github_url': project.github_url,
                'live_url': project.live_url,
                'image': project.image.url if project.image else None,
                'created_at': project.created_at.isoformat(),
            }
            projects_data.append(project_data)
        return JsonResponse({'projects': projects_data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_GET
def api_homepage(request):
    """API endpoint to get homepage data"""
    try:
        profile = Profile.objects.first()
        data = {
            'title': 'Portfolio - Home',
            'name': 'Kiesha Walker',
            'tagline': 'Software Engineer | Full Stack Developer',
            'profile': {
                'name': profile.name if profile else 'Kiesha Walker',
                'bio': profile.bio if profile else 'Software Engineer | Full Stack Developer',
                'profile_image': profile.profile_image.url if profile and profile.profile_image else None,
                'email': profile.email if profile else 'your.email@example.com',
            }
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
