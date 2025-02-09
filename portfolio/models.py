from django.db import models
from django.conf import settings

class Portfolio(models.Model):
    TEMPLATE_CHOICES = [
        ('template1', 'Modern Dark'),
        ('template2', 'Elegant Light'),
        ('template3', 'Professional Blue'),
        ('template4', 'Minimal White'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portfolio')
    title = models.CharField(max_length=255)
    description = models.TextField()
    template_choice = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, default='template1')
    github_link = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='portfolio/profile_images/', blank=True, null=True)
    resume = models.FileField(upload_to='portfolio/resumes/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='education')
    course = models.CharField(max_length=100)
    institute = models.CharField(max_length=255)
    result = models.CharField(max_length=50)
    year_of_passing = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course} from {self.institute}"

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    role = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    technologies = models.CharField(max_length=255)  # Comma-separated list of technologies used
    programming_languages = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    github_repo = models.URLField(blank=True, null=True)  # GitHub Project Link
    live_demo = models.URLField(blank=True, null=True)  # Live Code Demo URL
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Publication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=255)
    authors = models.TextField()
    journal = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    doi = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='certifications')
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    date_received = models.DateField()

    def __str__(self):
        return self.title

class Achievement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='achievements')
    description = models.TextField()

    def __str__(self):
        return self.description[:50]

class Skill(models.Model):
    SKILL_TYPES = [
        ('Programming Language', 'Programming Language'),
        ('Framework', 'Framework'),
        ('Tool', 'Tool'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)
    skill_type = models.CharField(max_length=30, choices=SKILL_TYPES, default='Other')

    def __str__(self):
        return f"{self.name} ({self.skill_type})"
