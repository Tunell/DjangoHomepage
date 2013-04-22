from django.conf.urls.defaults import *
from Pelle.minapp.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'minapp.views.index'),
    (r'^pager/$', 'minapp.views.pager'),
    (r'^allPosts/$', 'minapp.views.allPosts'),
    (r'^addSkiva/$', 'minapp.views.addSkiva'),
    (r'^addPost/$', 'minapp.views.addPost'),
    (r'^(?P<post_id>\d+)/$', 'minapp.views.showPost'),
    (r'^addComment/$', 'minapp.views.addComment'),
    (r'^(?P<post_id>\d+)/kommentera/$', 'minapp.views.kommentera'),
    (r'^tack/$', 'minapp.views.tack'),
    (r'^uppdatePost/$', 'minapp.views.uppdatePost'),
    (r'^(?P<post_id>\d+)/deletePost/$', 'minapp.views.deletePost'),
    (r'^(?P<comments_id>\d+)/deleteComment/$', 'minapp.views.deleteComment'),
#    (r'^inloggad/$', 'minapp.views.inloggad'),                    
    (r'^loginSvar/$', 'minapp.views.loginSvar'),                    
    (r'^login/$', 'minapp.views.loggaIn'),                     
    (r'^loggarIn/$', 'minapp.views.loggarIn'),                 
    (r'^logout/$', 'minapp.views.loggaUt'),        
    (r'^photologue/', include('photologue.urls')),
    (r'^hej/$', 'minapp.views.hej'),
    
    (r'^imageViewer/$', 'minapp.views.imageViewer'),
    (r'^laddaUppBild/$', 'minapp.views.laddaUppBild'),
    (r'^photologue/$', 'minapp.views.photologue'),
    (r'^addPic/$', 'minapp.views.addPic'),
    


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
