from django.db import models

#Nyheter
class News(models.Model):
    titel = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    
    #guestbook
class GuestbookPost(models.Model):
    nick = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    email = models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)