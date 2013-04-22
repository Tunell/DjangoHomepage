from django import forms
from ckeditor.widgets import CKEditorWidget

#Blogg inlagg
class BlogPost(forms.Form):
    Titel = forms.CharField(max_length=50)
    Text = forms.CharField(widget=CKEditorWidget())
    
#bild forsok   
class BildForm(forms.Form):
    titel = forms.CharField(max_length=50)
    fil = forms.ImageField()
#upload_to='bilder/%Y/Ym/%d'

#bild fosok
class ImageViewerForm(forms.Form):
#    tile = forms.CharField(max_length=50)
    image = forms.CharField(widget=CKEditorWidget())
