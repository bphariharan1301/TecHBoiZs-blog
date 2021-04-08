from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets
from myblog.models import Category, Profile
from .forms import ProfilePageForm, SignUpForm, EditProfileForm, PasswordChangingForm, UpdateProfilePageForm  
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.

class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profie_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

# User Registration 
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name =  'registration/register.html'
    success_url = reverse_lazy('login')

# Edit Profile
class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = UpdateProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    # fields = ['bio', 'profile_pic', 'portfolio_url', 'fb_url', 'insta_url', 'twitter_url', 'linkedin_url', 'pinterest_url']
    
    success_url = reverse_lazy('home')


# Update User Profile(Settings)
class UserUpdateView(generic.UpdateView):
    form_class = EditProfileForm
    model = Profile
    template_name =  'registration/edit_profile.html'
    # fields = ['username', 'first_name', 'last_name', ] #'portfolio_url', 'fb_url', 'insta_url', 'twitter_url', 'linkedin_url', 'pinterest_url']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserUpdateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

    def get_object(self):
        return self.request.user


    success_url = reverse_lazy('home')
    
class PasswordsUpdateView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})
    
