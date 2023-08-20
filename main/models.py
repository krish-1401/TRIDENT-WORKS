from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):


    user_name=models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    gender=models.CharField(max_length=10,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    city=models.CharField(max_length=200,null=True,blank=True)
    profession=models.CharField(max_length=20,null=True,blank=True)
    fees=models.FloatField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True,default='image.jpg')

    @property
    def imageURL(self):
        try:
            url=self.profile_image.url
        except:
            url=''
        return url  
    def __str__(self):
        return self.user_name.username