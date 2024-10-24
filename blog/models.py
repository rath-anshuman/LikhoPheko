from django.db import models

from useraccount.models import UserAccount

class Blog(models.Model):
    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name="usercreated")
    title=models.CharField(max_length=50,blank=False,null=False)
    starttext=models.CharField(max_length=5000,blank=False,null=False)
    media=models.CloudinaryField('image', folder=f'AnishBlogs/{user}/',null=True)
    endtext=models.CharField(max_length=5000,blank=False,null=False)
