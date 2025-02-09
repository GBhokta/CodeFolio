from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PortfolioForm, EducationForm, ProjectForm, PublicationForm, CertificationForm, SkillForm

from django.shortcuts import render, get_object_or_404

from portfolio.models import Portfolio, Education, Project, Publication, Certification, Achievement, Skill
from accounts.models import UserProfile  
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from .models import Portfolio

@login_required
def change_template(request):
    if request.method == "POST":
        data = json.loads(request.body)
        template_choice = data.get("template_choice")

        if template_choice:
            portfolio, created = Portfolio.objects.get_or_create(user=request.user)
            portfolio.template_choice = template_choice
            portfolio.save()
            return JsonResponse({"status": "success", "message": "Template updated successfully"})
        
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


def view_portfolio(request, username):
    portfolio = get_object_or_404(Portfolio, user__username=username)
    user_profile = get_object_or_404(UserProfile, user=portfolio.user)  # ✅ Fetch UserProfile
    
    # ✅ Dynamic template based on user selection
    template = f"portfolio/{portfolio.template_choice}.html"

    context = {
        'portfolio': portfolio,
        'user_profile': user_profile,  # ✅ Add user profile details
        'educations': Education.objects.filter(user=portfolio.user),
        'projects': Project.objects.filter(user=portfolio.user),
        'publications': Publication.objects.filter(user=portfolio.user),
        'certifications': Certification.objects.filter(user=portfolio.user),
        'achievements': Achievement.objects.filter(user=portfolio.user),
        'skills': Skill.objects.filter(user=portfolio.user),
    }

    return render(request, template, context)


@login_required
def create_or_edit_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)

    # ✅ Create formsets with delete functionality
    EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1, can_delete=True)
    ProjectFormSet = modelformset_factory(Project, form=ProjectForm, extra=1, can_delete=True)
    PublicationFormSet = modelformset_factory(Publication, form=PublicationForm, extra=1, can_delete=True)
    CertificationFormSet = modelformset_factory(Certification, form=CertificationForm, extra=1, can_delete=True)
    SkillFormSet = modelformset_factory(Skill, form=SkillForm, extra=1, can_delete=True)

    if request.method == 'POST':
        portfolio_form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        education_formset = EducationFormSet(request.POST, queryset=Education.objects.filter(user=request.user))
        project_formset = ProjectFormSet(request.POST, queryset=Project.objects.filter(user=request.user))
        publication_formset = PublicationFormSet(request.POST, queryset=Publication.objects.filter(user=request.user))
        certification_formset = CertificationFormSet(request.POST, queryset=Certification.objects.filter(user=request.user))
        skill_formset = SkillFormSet(request.POST, queryset=Skill.objects.filter(user=request.user))

        if portfolio_form.is_valid():
            portfolio_form.save()

        # ✅ Loop through each formset and handle deletions/new entries
        for formset in [education_formset, project_formset, publication_formset, certification_formset, skill_formset]:
            if formset.is_valid():
                instances = formset.save(commit=False)  # Save instances but don't commit yet
                for instance in instances:
                    instance.user = request.user  # Assign current user
                    instance.save()  # Save instance to the database

                for form in formset.deleted_forms:  # ✅ Handle deletions
                    form.instance.delete()

        return redirect('view_portfolio', username=request.user.username)

    else:
        portfolio_form = PortfolioForm(instance=portfolio)
        education_formset = EducationFormSet(queryset=Education.objects.filter(user=request.user))
        project_formset = ProjectFormSet(queryset=Project.objects.filter(user=request.user))
        publication_formset = PublicationFormSet(queryset=Publication.objects.filter(user=request.user))
        certification_formset = CertificationFormSet(queryset=Certification.objects.filter(user=request.user))
        skill_formset = SkillFormSet(queryset=Skill.objects.filter(user=request.user))

    return render(request, 'portfolio/portfolio_form.html', {
        'portfolio_form': portfolio_form,
        'education_formset': education_formset,
        'project_formset': project_formset,
        'publication_formset': publication_formset,
        'certification_formset': certification_formset,
        'skill_formset': skill_formset,
    })


@login_required
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .models import Portfolio, Education, Project, Publication, Certification, Achievement, Skill
from .forms import PortfolioForm, EducationForm, ProjectForm, PublicationForm, CertificationForm, AchievementForm, SkillForm



# ✅ Add/Edit/Delete Views for Education
@login_required
def add_or_edit_education(request, pk=None):
    if pk:
        education = get_object_or_404(Education, pk=pk, user=request.user)
    else:
        education = Education(user=request.user)

    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('view_portfolio', username=request.user.username)
    else:
        form = EducationForm(instance=education)

    return render(request, 'portfolio/edit_education.html', {'form': form})

@login_required
def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        education.delete()
        return redirect('view_portfolio', username=request.user.username)
    return render(request, 'portfolio/delete_item.html', {'item': education})

# ✅ Add/Edit/Delete Views for Projects
@login_required
def add_or_edit_project(request, pk=None):
    if pk:
        project = get_object_or_404(Project, pk=pk, user=request.user)
    else:
        project = Project(user=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('view_portfolio', username=request.user.username)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'portfolio/edit_project.html', {'form': form})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('view_portfolio', username=request.user.username)
    return render(request, 'portfolio/delete_item.html', {'item': project})

# ✅ Add/Edit/Delete Views for Skills
@login_required
def add_or_edit_skill(request, pk=None):
    if pk:
        skill = get_object_or_404(Skill, pk=pk, user=request.user)
    else:
        skill = Skill(user=request.user)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('view_portfolio', username=request.user.username)
    else:
        form = SkillForm(instance=skill)

    return render(request, 'portfolio/edit_skill.html', {'form': form})

@login_required
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        skill.delete()
        return redirect('view_portfolio', username=request.user.username)
    return render(request, 'portfolio/delete_item.html', {'item': skill})
