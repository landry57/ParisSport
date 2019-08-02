from django.urls import path,re_path
from .import views
app_name='blog'
urlpatterns = [
    #path('', views.index, name='index'),
    #re_path(r'^posts/(?P<id>[0-9]+)',views.show,name='show'),
    path('accueil', views.accueil, name='accueil'),
    path('connexion', views.connexion, name='connexion'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.Register, name='register'),
    path('paris', views.paris, name='paris'),


]
