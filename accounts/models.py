from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(null=True,blank=True)
    profile_image=models.ImageField(upload_to='profiles/',null=True,blank=True)
    linkedin=models.URLField(null=True,blank=True)
    github=models.URLField(null=True,blank=True)
    twitter=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.user.username
    
    @receiver(post_save,sender=User)
    def create_or_update_user_profile(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()
# Create your models here.
