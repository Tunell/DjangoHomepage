# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from sidan.models import News, GuestbookPost
from sidan.forms import *
from ckeditor.fields import RichTextField
import photologue

def news(request):
    news_list = News.objects.all().order_by("-pub_date")
    paginator = Paginator(news_list, 3)
    page = int(request.GET.get('page', '1')) 
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render_to_response('news.html', locals())

#Visa och redigera blogg inlagg
def showNews(request, post_id):
    news = News.objects.get(pk = post_id)
    return render_to_response('news.html', locals())

#redigera blogg inlagg
def uppdateNews(request):
    news_id = request.GET['id']
    nyNewsTitel = request.GET['titel']
    text = request.GET['body']
    news = News.objects.get(pk = news_id)
    news.titel = nyNewsTitel
    news.body = text
    news.save()
    return HttpResponseRedirect(reverse('sidan.views.news'))

#Ta bort newspost    
def deleteNews(request, news_id):
    news = News.objects.get(pk = news_id)
    news.delete()
    return HttpResponseRedirect('/')

def allNews(request):
    all_news = News.objects.all().order_by("-pub_date")
    return render_to_response('allNews.html', locals())

def omOss(request):
    return render_to_response('omOss.html', locals())

def links(request):
    return render_to_response('links.html', locals())

def kontakt(request):
    return render_to_response('kontakt.html', locals())

def medlemmar(request):
    return render_to_response('medlemmar.html', locals())

def bilder(request):
    return render_to_response('bilder.html', locals())

def filmer(request):
    return render_to_response('filmer.html', locals())
    
def addNews(request):
    if request.user.is_authenticated():
        if request.method != 'POST':
            form = NewsForm()
        else:
            form = NewsForm(request.POST)
            if form.is_valid():
                rubrik = form.cleaned_data['Titel']
                text = form.cleaned_data['Text']
                nyNews = News(titel = rubrik, body = text)
                nyNews.save()
                return HttpResponseRedirect(reverse('sidan.views.news'))
    
        return render_to_response('addNews.html', locals())
    else:
        return HttpResponseRedirect('/login/')
    
def guestbook(request):
    
    post_list = GuestbookPost.objects.all()
    paginator = Paginator(post_list, 6)
    page = int(request.GET.get('page', '1')) 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if request.method != 'POST':
        form = guestbookForm()
    else:
        form = guestbookForm(request.POST)
        if form.is_valid():
            namn = form.cleaned_data['nick']
            Text = form.cleaned_data['text']
            Email = form.cleaned_data['email']
            nyPost = GuestbookPost(nick = namn, text = Text, email = Email)
            nyPost.save()
            return HttpResponseRedirect(reverse('sidan.views.guestbook'))
    return render_to_response('guestbook.html', locals())