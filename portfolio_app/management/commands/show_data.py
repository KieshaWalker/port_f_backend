from django.core.management.base import BaseCommand
from portfolio_app.models import Profile, Project

class Command(BaseCommand):
    help = 'Display all portfolio data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== PROFILES ==='))
        for profile in Profile.objects.all():
            self.stdout.write(f'ID: {profile.id}')
            self.stdout.write(f'Name: {profile.name}')
            self.stdout.write(f'Email: {profile.email}')
            self.stdout.write(f'Bio: {profile.bio[:100]}...')
            if profile.profile_image:
                self.stdout.write(f'Profile Image: {profile.profile_image.url}')
            self.stdout.write('---')

        self.stdout.write(self.style.SUCCESS('\n=== PROJECTS ==='))
        for project in Project.objects.all():
            self.stdout.write(f'ID: {project.id}')
            self.stdout.write(f'Name: {project.name}')
            self.stdout.write(f'Description: {project.description[:100]}...')
            self.stdout.write(f'Technologies: {project.technologies}')
            if project.github_url:
                self.stdout.write(f'GitHub: {project.github_url}')
            if project.live_url:
                self.stdout.write(f'Live URL: {project.live_url}')
            if project.image:
                self.stdout.write(f'Image: {project.image.url}')
            self.stdout.write(f'Created: {project.created_at}')
            self.stdout.write('---')