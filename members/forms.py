from io import SEEK_CUR
from myblog.models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm #, AuthenticationForm 
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'portfolio_url', 'fb_url', 'insta_url', 'twitter_url', 'linkedin_url', 'pinterest_url')

        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            # 'profile_pic' : forms.Select(attrs={'class':'form-control'}),
            'portfolio_url' : forms.TextInput(attrs={'class':'form-control'}),
            'fb_url' : forms.TextInput(attrs={'class':'form-control'}),
            'insta_url' : forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url' : forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url' : forms.TextInput(attrs={'class':'form-control'}),
            'pinterest_url' : forms.TextInput(attrs={'class':'form-control'}),
        }
class UpdateProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'portfolio_url', 'fb_url', 'insta_url', 'twitter_url', 'linkedin_url', 'pinterest_url')

        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            # 'profile_pic' : forms.Select(attrs={'class':'form-control'}),
            'portfolio_url' : forms.TextInput(attrs={'class':'form-control'}),
            'fb_url' : forms.TextInput(attrs={'class':'form-control'}),
            'insta_url' : forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url' : forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url' : forms.TextInput(attrs={'class':'form-control'}),
            'pinterest_url' : forms.TextInput(attrs={'class':'form-control'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def __init__(self, *args, **kawrgs):
        super(SignUpForm, self).__init__(*args,**kawrgs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class EditProfileForm(forms.ModelForm):
    # bio = forms.Textarea(widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Profile
        # fields = ('username', 'first_name', 'last_name', 'email',)
        fields = ( 'username', 'first_name', 'last_name', 'email')
        # fields = '__all__'

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
# type="password"
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


