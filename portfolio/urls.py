from django.urls import path
from .views import (
    portfolio_list, create_or_edit_portfolio, view_portfolio,
    add_or_edit_education, delete_education,
    add_or_edit_project, delete_project,
    add_or_edit_skill, delete_skill,change_template
)

urlpatterns = [
    path("change-template/", change_template, name="change_template"),
    path('', portfolio_list, name='portfolio_list'),  # ✅ Now included
    path('edit/', create_or_edit_portfolio, name='edit_portfolio'),
    path('<str:username>/', view_portfolio, name='view_portfolio'),

    # Education
    path('education/add/', add_or_edit_education, name='add_education'),
    path('education/<int:pk>/', add_or_edit_education, name='edit_education'),
    path('education/<int:pk>/delete/', delete_education, name='delete_education'),

    # Projects
    path('project/add/', add_or_edit_project, name='add_project'),
    path('project/<int:pk>/', add_or_edit_project, name='edit_project'),
    path('project/<int:pk>/delete/', delete_project, name='delete_project'),

    # Skills
    path('skill/add/', add_or_edit_skill, name='add_skill'),
    path('skill/<int:pk>/', add_or_edit_skill, name='edit_skill'),
    path('skill/<int:pk>/delete/', delete_skill, name='delete_skill'),
]
