
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django import forms

class CustomSignupForm(UserCreationForm):
    

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)  
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label     
        self.fields["first_name"].widget.attrs["placeholder"] = self.fields["first_name"].label
        self.fields['last_name'].widget.attrs['placeholder']=self.fields['last_name'].label
        self.fields['password1'].widget.attrs['placeholder']=self.fields['password1'].label
        self.fields['password2'].widget.attrs['placeholder']=self.fields['password2'].label
        
    class Meta:
        model = myuser
        fields =('email', 'first_name', 'last_name', "password1", 'password2')


class myloginform(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'Placeholder':'Email'}))
    password = forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={'placeholder': "Password"}))


class CommentForm(forms.ModelForm):
    class Meta:
        model=BlogComment
        fields = ('body', 'parent')