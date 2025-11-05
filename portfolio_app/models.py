from django.db import models

class Profile(models.Model):
    """Profile model for personal information and profile picture"""
    name = models.CharField(max_length=100, default="Your Name")
    bio = models.TextField(default="Your bio goes here...")
    profile_image = models.ImageField(upload_to='images/profiles/', blank=True, null=True)
    email = models.EmailField(default="your.email@example.com")

    def __str__(self):
        return self.name

class Project(models.Model):
    """Project model with image support"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_technologies_list(self):
        """Return technologies as a list"""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
