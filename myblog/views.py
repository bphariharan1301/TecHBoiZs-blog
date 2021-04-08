from django import forms
from django.db import connection
from django.forms import fields
from django.http import request, HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Comment, Post, Profile
from .forms import EditForm, PostForm, CommentForm 
# Create your views here.

class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-published_date']
    # categories dropdown
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

class CommentView(CreateView):
    # def add_comment():
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    context = Post.id 
    # def add_comment():
    #     context = Post.id
    #     return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

    success_url = reverse_lazy('home')

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        values = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = values.total_likes()
        
        # total_dislikes = values.total_dislikes()
        liked = False
        if values.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] =  liked
        context["cat_menu"] =  cat_menu
        context["total_likes"] =  total_likes
        # context["total_dislikes"] = total_dislikes
        return context
    def Comment():
        model = Comment
        form_class = CommentForm
        template_name = 'article_detail.html'
        def form_valid(self, form):
            form.instance.post_id = self.kwargs['pk']
            return super().form_valid(forms)

        success_url = reverse_lazy('home') 


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    # fields = '__all__' # To fetch all the fields from the database of post for the add post form 
    # fields = ('title', 'author', 'body') # To fetch selected fields from database for the add post form

    # We dont need the fields var since the forms.py will take care of those froms stuffs


def CategoryView(request, cats):
    category_post = Post.objects.filter(category = cats.replace('-', ' '))    
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_post':category_post})



class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

'''def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})'''

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'

    def get_context_data(self, *args ,**kwargs):
        cat_menu = Category.objects.all()
        cat_menu_list = Category.objects.all()
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["cat_menu_list"] = cat_menu_list
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False 
    else:
        post.likes.add(request.user)  
        liked = True 
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))







    