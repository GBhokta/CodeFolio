from django import forms
from .models import Portfolio, Education, Project, Publication, Certification, Achievement, Skill

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'template_choice', 'github_link', 'linkedin', 'twitter', 'website', 'profile_image', 'resume']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['course', 'institute', 'result', 'year_of_passing']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'role', 'description', 'start_date', 'end_date', 'technologies', 'programming_languages', 'link', 'github_repo', 'live_demo', 'image']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'authors', 'journal', 'year', 'doi']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['title', 'issuer', 'date_received']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['description']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency', 'skill_type']
