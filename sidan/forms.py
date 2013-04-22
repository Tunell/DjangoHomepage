from django import forms
from ckeditor.widgets import CKEditorWidget

#Nyhet
class NewsForm(forms.Form):
    Titel = forms.CharField(max_length=50)
    Text = forms.CharField(widget=CKEditorWidget())
    
#guestbook
class guestbookForm(forms.Form):
    nick = forms.CharField(max_length=50)
    Text = forms.CharField(max_length=1000)
    email = forms.EmailField()
    
    