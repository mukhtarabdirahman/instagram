from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    profilePic = models.ImageField(upload_to='profile/',null=True)
    bio = models.CharField(max_length=60,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def update_profile(cls,id,bio):
        updated = Image.objects.filter(id=id).update(bio = bio)
        return updated

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', null=True)
    caption = models.CharField(max_length = 60)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.caption
    class Meta:
        ordering = ['-upload_date']

    def save_image(self):
        self.save()


    
    
    
