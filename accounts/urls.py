from django.urls import path
from .views import register, edit_profile,logout_v
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('register/', register, name='register'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',logout_v , name='logout'),
    

]
