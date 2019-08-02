from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.sessions.models import Session
#from .mocks import Post
from .models import Post,Paris,Compte
from django.contrib.auth.models import User
from .forms import LoginForm, Register
"""
def index(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

def show(request,id):
    post = Post.objects.get(pk=id)
    return render(request,'blog/show.html',{'post':post})
"""
def accueil(request):
    if  request.session.has_key('username'):
        return render(request,'blog/accueil.html')
    else:
        return render(request,'blog/connexion.html')


def connexion(request):
    if  request.session.has_key('username'):
        return render(request,'blog/accueil.html')
    else:
        return render(request,'blog/connexion.html')



def paris(request):
    return render(request,'blog/paris.html')
    if request.method == 'POST':
        id= request.session['id']
        p=Paris(vs='errro',person_id=id)
        p.save()

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    data = User.objects.get(username=request.POST['username'])
    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      request.session['firstname'] = data.first_name
      request.session['lastname'] = data.last_name
      request.session['id'] = data.id
      return render(request,'blog/accueil.html',{})

    else:

      return HttpResponseRedirect('connexion')
  else:
      if  request.session.has_key('username'):
           return render(request,'blog/accueil.html')
      else:
          return render(request,'blog/connexion.html')



####################Register



def Register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['passwd']
        password2 = request.POST['passwd2']

        if (( email !='') and (password == password2)):
            if User.objects.filter(email=email).exists():
              return  HttpResponseRedirect('connexion')
            else:
               user = User.objects.create_user(username=username,password=password, first_name=first_name ,email=email, last_name=last_name)
               user.save()
               return  HttpResponseRedirect('connexion')
        else:
            return  HttpResponseRedirect('connexion')
    else:
        return  HttpResponseRedirect('connexion')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return HttpResponseRedirect('connexion')
