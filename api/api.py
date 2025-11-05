import os
from ninja import NinjaAPI

from portfolio_app.models import Profile, Project
api = NinjaAPI()

@api.get("/profile")
def api_profile(request):
    """API endpoint to get profile data"""
    try:
        # For serverless environment, return sample data to avoid database issues
        if os.environ.get('VERCEL') or os.environ.get('VERCEL_ENV'):
            return {
                'name': 'Kiesha Walker',
                'bio': 'Software Engineer | Full Stack Developer',
                'email': 'kiesha@example.com',
                'profile_image': None,
            }

        profile = Profile.objects.first()
        if profile:
            data = {
                'name': profile.name,
                'bio': profile.bio,
                'email': profile.email,
                'profile_image': profile.profile_image.url if profile.profile_image else None,
            }
        else:
            data = {
                'name': 'Kiesha Walker',
                'bio': 'Software Engineer | Full Stack Developer',
                'email': 'your.email@example.com',
            }
        return data
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

@api.get("/projects")
def api_projects(request):
    """API endpoint to get projects data"""
    try:
        # For serverless environment, return sample data to avoid database issues
        if os.environ.get('VERCEL') or os.environ.get('VERCEL_ENV'):
            return {"projects": [
                {
                    'id': 1,
                    'name': 'Portfolio Website',
                    'description': 'A modern, responsive portfolio website built with Django and Bootstrap.',
                    'technologies': ['Django', 'Python', 'HTML', 'CSS', 'Bootstrap', 'JavaScript'],
                    'github_url': 'https://github.com/username/portfolio',
                    'live_url': 'https://yourportfolio.com',
                    'image': None,
                    'created_at': '2025-11-04T00:00:00Z',
                },
                {
                    'id': 2,
                    'name': 'Task Management App',
                    'description': 'A collaborative task management application with real-time updates.',
                    'technologies': ['React', 'Node.js', 'MongoDB', 'Socket.io'],
                    'github_url': 'https://github.com/username/taskmanager',
                    'live_url': 'https://taskmanager.com',
                    'image': None,
                    'created_at': '2025-11-03T00:00:00Z',
                }
            ]}

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

        # If no projects in database, return sample data
        if not projects_data:
            projects_data = [
                {
                    'id': 1,
                    'name': 'Portfolio Website',
                    'description': 'A modern, responsive portfolio website built with Django and Bootstrap.',
                    'technologies': ['Django', 'Python', 'HTML', 'CSS', 'Bootstrap', 'JavaScript'],
                    'github_url': 'https://github.com/username/portfolio',
                    'live_url': 'https://yourportfolio.com',
                    'image': None,
                    'created_at': '2025-11-04T00:00:00Z',
                },
                {
                    'id': 2,
                    'name': 'Task Management App',
                    'description': 'A collaborative task management application with real-time updates.',
                    'technologies': ['React', 'Node.js', 'MongoDB', 'Socket.io'],
                    'github_url': 'https://github.com/username/taskmanager',
                    'live_url': 'https://taskmanager.com',
                    'image': None,
                    'created_at': '2025-11-03T00:00:00Z',
                }
            ]

        return {"projects": projects_data}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}