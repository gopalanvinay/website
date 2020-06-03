from django import forms
from .models import Mails

class EmailForm(forms.ModelForm):

    name = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    message = forms.CharField( widget=forms.Textarea(attrs={'class': "form-control"}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))
    
    class Meta:
        model = Mails
        fields = ('email','subject','message')