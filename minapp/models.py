from django.db import models

#Blogginlagg
class Post(models.Model):
    titel = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)

#Kommentarer
class Comments(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateTimeField(auto_now = True)
    key = models.ForeignKey(Post)

#forsok pa bilder    
class Bilder(models.Model):
    titel = models.CharField(max_length=50)
    file = models.ImageField(upload_to='bilder/%Y/Ym/%d')

#dumt och daligt forsok pa anvandare
#class Users(models.User):
#    username = models.CharField(max_length=30)
    
    
"""    
class Skiva(models.Model):
    namn = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
"""