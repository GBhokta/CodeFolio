from django.contrib import admin
from .models import Education, Project, Skill, Publication, Certification, Achievement

# Register your models here.
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Publication)
admin.site.register(Certification)
admin.site.register(Achievement)

