from django.urls import path
from .views import AddCategoryView, Home, ArticleDetail, AddPostView,  LikeView, UpdatePostView, DeletePostView, CategoryView, CategoryListView , CommentView
# LikeView HomeLikeView,
# from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    # path('article/<int:pk>/comment', CommentView.as_view(), name='add_comment'),
    # path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category-list/', CategoryListView.as_view(), name='category_list'),
    path('category/<str:cats>/', CategoryView, name='category'),
    # path('category-list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    # path('like/<int:pk>', HomeLikeView, name='like_post_home'),
    # path('add_category/', AddCategoryView.as_view(), name='add_category'),
    # path('', views.home, name='home') in case if you are using function
    path('article/<int:pk>/comment/', CommentView.as_view(), name='add_comment'),
]
