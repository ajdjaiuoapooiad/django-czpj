from django.db import models





class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255,null=True,blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True,blank=True)
    facebook_link = models.URLField(max_length=100,null=True,blank=True)
    twitter_link = models.URLField(max_length=100,null=True,blank=True)
    google_plus_link = models.URLField(max_length=100,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
