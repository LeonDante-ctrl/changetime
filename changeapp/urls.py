from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome, name="main"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/<str:username>/', views.profile, name = 'profile'),
    path('update_profile', views.update_profile, name="update_profile"),
    path('post/article', views.article, name='newArticle'),
    path('delete/article/<int:id>', views.delete_article, name = 'delete_article'),
    path('edit/article/<int:id>', views.update_article, name ='update_article'),
    path('article/<int:id>', views.single_article, name = 'single_article')

]
