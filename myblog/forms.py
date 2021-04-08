from os import name
from django import forms
from django.forms import fields
from django.forms import widgets
from .models import Category, Comment, Post

# choices = [('coding', 'coding'), ('technology','technology'), ('sports','sports'),]

choices = Category.objects.all().values_list('name','name')
choice_list = []

for i in choices:
    choice_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author','category', 'header_image', 'snippet','body')
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.Select(attrs={'class':'form-control'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder'}),
            'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            # 'category' : forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'snippet', 'header_image', 'body')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sectumsempra Spell'}),
            'body' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'For enemies'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
        }


'''class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the Category'})
        }

        choice_list.append(name)'''


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name'  : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}) # body of the comment
        }
