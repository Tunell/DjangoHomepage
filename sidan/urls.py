from django.conf.urls.defaults import *
from Pelle.minapp.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^news/$', 'sidan.views.news'),
    (r'^(?P<post_id>\d+)/edit/$', 'minapp.views.showNews'),
    (r'^uppdateNews/$', 'minapp.views.uppdateNews'),
    (r'^(?P<news_id>\d+)/deleteNews/$', 'minapp.views.deleteNews'),
    (r'^allNews/$', 'sidan.views.allNews'),
    (r'^addNews/$', 'sidan.views.addNews'),
    (r'^omOss/$', 'sidan.views.omOss'),
    (r'^links/$', 'sidan.views.links'),
    (r'^medlemmar/$', 'sidan.views.medlemmar'),
    (r'^bilder/$', 'sidan.views.bilder'),
    (r'^filmer/$', 'sidan.views.filmer'),
    (r'^kontakt/$', 'sidan.views.kontakt'),
    (r'^guestbook/$', 'sidan.views.guestbook'),
    
    


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
