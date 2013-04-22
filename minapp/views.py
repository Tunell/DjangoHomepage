# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from minapp.models import Post, Comments, Bilder
from minapp.forms import *
from ckeditor.fields import RichTextField
import photologue

 
#Visar login sidan
def loggaIn(request):
    return render_to_response('login.html', locals())


#Visar login sidan om man gor nagot fel(maste finnas eftersom det ibland skickas med user)
def loginSvar(request, user):
    return render_to_response('login.html', locals())

#Inloggnings funktionen
def loggarIn(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/loginSvar/')
    else:
        return HttpResponseRedirect('/login/')
    
#logga ut knapp    
def loggaUt(request):
    logout(request)
    return HttpResponseRedirect('/')

#Forsta sidan i bloggen for icke inloggade anvandare. visar 6 blogg inlagg
def index(request):
    post_list = Post.objects.all().order_by("-pub_date")
    paginator = Paginator(post_list, 6)
    page = int(request.GET.get('page', '1'))
    antalKommentarer = Comments.objects.count()
    #antalKommentarer = Comments.objects.filter(Post.pk==Comments.key).count()
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render_to_response('index.html', locals())

#Sumerings sida med alla blog inlagg
def allPosts(request):
    all_posts = Post.objects.all().order_by("-pub_date")
    return render_to_response('allPosts.html', locals())

#Lagg till blog post funktion
def addPost(request):
    if request.user.is_authenticated():
        if request.method != 'POST':
            form = BlogPost()
        else:
            form = BlogPost(request.POST)
            if form.is_valid():
                rubrik = form.cleaned_data['Titel']
                text = form.cleaned_data['Text']
                nyPost = Post(titel = rubrik, body = text)
                nyPost.save()
                return HttpResponseRedirect(reverse('minapp.views.index'))
    
        return render_to_response('addPost.html', locals())
    else:
        return HttpResponseRedirect('/login/')

#Visa och redigera blogg inlagg
def showPost(request, post_id):
    post = Post.objects.get(pk = post_id)
    commentsa = Comments.objects.all().filter(key=post_id).order_by("-date")
    return render_to_response('post.html', locals())

#redigera blogg inlagg
def uppdatePost(request):
    post_id = request.GET['id']
    nyPostTitel = request.GET['titel']
    text = request.GET['body']
    post = Post.objects.get(pk = post_id)
    post.titel = nyPostTitel
    post.body = text
    post.save()
    return HttpResponseRedirect(reverse('minapp.views.index'))

#Ta bort blogpost    
def deletePost(request, post_id):
    post = Post.objects.get(pk = post_id)
    post.delete()
    return HttpResponseRedirect('/')

#Kommentera ett blog inlagg
def addComment(request):
    pi = request.GET['id']
    name = request.GET['name']
    kommentar = request.GET['comment']
    post = Post.objects.get(pk = pi)    
    nyKommentar = Comments(key=post, name=name, comment=kommentar)
    nyKommentar.save()
    return HttpResponseRedirect(reverse('minapp.views.tack'))


def kommentera(request, post_id):
    post = Post.objects.get(pk = post_id)
    commentsa = Comments.objects.all().filter(key=post_id).order_by("-date")
    return render_to_response('kommentera.html', locals())

def tack(request):
    return render_to_response('tack.html', locals())

#Ta bort kommentar
def deleteComment(request, comments_id):
    comments = Comments.objects.get(pk = comments_id)
    comments.delete()
    return HttpResponseRedirect('/index/')


#test funktion for bland annat att se om man ar inloggad
def hej(request):
    if request.user.is_authenticated():
        return HttpResponse ('Hej')
    else:
        return HttpResponseRedirect('/login/')

# (Borde kunna tas bort men blir anropad pa nagot konstigt satt)   
def deleteNews(request):
    pass

# (Borde kunna tas bort men blir anropad pa nagot konstigt satt)    
def uppdateNews(request):
    pass

# (Borde kunna tas bort men blir anropad pa nagot konstigt satt)   
def showNews(request):
    pass
    
# (Borde kunna tas bort men blir anropad pa nagot konstigt satt)
def pager(request):
    pass

# Gammal metod for att legga in ett blogg inlegg.(Borde kunna tas bort men blir anropad pa nagot konstigt satt)
def addSkiva(request):
    if request.user.is_authenticated():
        vald_titel = request.POST['skiv_namn']
        text = request.POST['body_text']
        nySkiva = Post(titel = vald_titel, body = text)
        nySkiva.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

#Har borjar massa kod som inte anvands for tillfallet i sidan. Det ar massa olika forsok pa funktioner som jag lost pa annat vis.
#forsok pa bild funktion
def addPic(request):
    valdTitel = request.POST['titel']
    valdFil = request.POST['fil']
    newPic = Bilder(titel = valdTitel, file = valdFil)
    newPic.save()
    return HttpResponseRedirect('/')


#forsok pa bild funktion
def laddaUppBild(request):
    if request.method == 'POST': # If the form has been submitted...
        form = BildForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            titel = form.cleaned_data['titel']
            nyBild = Bilder(titel=titel)
            nyBild.save()
            return HttpResponseRedirect(reverse('minapp.views.index'))# Redirect after POST
    else:
        form = BildForm() # An unbound form

    return render_to_response('laddaUppBild.html', locals())

#forsok pa bild funktion
def imageViewer(request):
    if request.method != 'POST':
        form = ImageViewerForm()
    else:
        form = ImageViewerForm(request.POST, request.FILES)
        if form.is_valid():
            uploadedImage = form.cleaned_data['image']
            filename = uploadedImage.filename
            imageData = uploadedImage.content
#            imageData = flip(imageData)
            return HttpResponse(imageData, mimetype="image/jpg")

    return render_to_response('imageViewer.html', locals())


#forsok pa bild funktion
def photologue(request):
    return render_to_response('gallery_archive.html', locals())

'''def upload_file(request):
    if request.method == 'POST':
        form = Bilder(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})

def handle_uploaded_file(f):
    destination = open('some/file/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
'''

""""Gammal funktion for att redigera blogg inlagg for inloggade anvandare
def editPost(request, post_id):
    post = Post.objects.get(pk = post_id)
    commentsa = Comments.objects.all().filter(key=post_id).order_by("-date")
#    comments = post.comments_set.all()
    return render_to_response('editpost.html', locals())
"""

'''def upload_file(request):
    if request.method == 'POST':
        form = Bilder(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})

def handle_uploaded_file(f):
    destination = open('some/file/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
'''

'''def upload_file(request):
    if request.method == 'POST':
        form = Bilder(request.POST, request.FILES)
        handle_uploaded_file(request.FILES['file'])

def handle_uploaded_file(f):
    destination = open('/Bilder/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
'''   


"""Onodig gammal Index sida for inloggade anvandare    
def inloggad(request):
    all_posts = Post.objects.all().order_by("-pub_date")
    if request.user.is_authenticated():
        return render_to_response('inloggad.html', locals())
    else:
        return render_to_response('index.html', locals())
"""
 
"""Gammal dalig(icke fungerande) hemmagjord pager version

def sorterar(request):
    start_id = (1)
    end_id = (3)
    posts = Post.objects.filter(pk__range=(start_id, end_id)).order_by("-pub_date")
#vand pa ordningen
    if request.user.is_authenticated():
        return render_to_response('sortera.html', {'posts': posts})
    else:
        return render_to_response('sortera.html', {'posts': posts})    

def sortera(request, n):
    num = int(n)
    start_id = (num*10-9)
    end_id = (num*10+1)
    posts = Post.objects.filter(pk__range=(start_id, end_id))
    
    topPost = Post.objects.count()
    topSite = topPost/10
    
    return render_to_response('index.html', locals())
#vand pa ordningen


 if request.user.is_authenticated():
        return render_to_response('sortera.html', {'posts': posts})
    else:"""
