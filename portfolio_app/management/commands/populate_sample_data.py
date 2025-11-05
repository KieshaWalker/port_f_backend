from django.core.management.base import BaseCommand
from portfolio_app.models import Profile, Project

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Create sample profile
        profile, created = Profile.objects.get_or_create(
            name="Your Name",
            defaults={
                'bio': 'I am a passionate developer with experience in various technologies. I love creating innovative solutions and learning new things.',
                'email': 'your.email@example.com'
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Created sample profile'))
        else:
            self.stdout.write('Profile already exists')

        # Create sample projects
        projects_data = [
            {
                'name': 'Portfolio Website',
                'description': 'A modern, responsive portfolio website built with Django and Bootstrap. Features clean design, smooth animations, and mobile-first approach.',
                'technologies': 'Django, Python, HTML, CSS, Bootstrap, JavaScript',
                'github_url': 'https://github.com/username/portfolio',
                'live_url': 'https://yourportfolio.com'
            },
            {
                'name': 'E-commerce Platform',
                'description': 'Full-stack e-commerce solution with user authentication, payment processing, and admin dashboard. Built with modern web technologies.',
                'technologies': 'React, Node.js, Express, MongoDB, Stripe API',
                'github_url': 'https://github.com/username/ecommerce',
                'live_url': 'https://yourshop.com'
            },
            {
                'name': 'Task Management App',
                'description': 'A collaborative task management application with real-time updates, team collaboration features, and progress tracking.',
                'technologies': 'Vue.js, Firebase, Tailwind CSS, WebSocket',
                'github_url': 'https://github.com/username/taskmanager',
                'live_url': 'https://taskmanager.com'
            }
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                name=project_data['name'],
                defaults=project_data
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created project: {project.name}'))
            else:
                self.stdout.write(f'Project already exists: {project.name}')

        self.stdout.write(self.style.SUCCESS('Sample data population complete!'))