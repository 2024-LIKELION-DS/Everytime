from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, logout
from .forms import *
from post.models import Post
from user.models import User

# Create your views here.

def signup_view(request):
  if request.method == "GET":
    form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
  
  form = SignUpForm(request.POST)

  if form.is_valid():
    user = form.save()
    return redirect('accounts:login')
  else: return render(request, 'accounts/signup.html', {'form':form})


def login_view(request):
  if request.method == "GET":
    return render(request, 'accounts/login.html', {'form': AuthenticationForm})
  
  form = AuthenticationForm(request, data=request.POST)

  if form.is_valid():
    login(request, form.user_cache)
    return redirect("post:home")
  return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
  if request.user.is_authenticated:
    logout(request)
  return redirect("post:list")

def mypage(request):
  return render(request, 'accounts/mypage.html')


def write_list(request):
  posts = request.user.post_user.all()
  return render(request, 'accounts/write_list.html', {'posts': posts})


def scrap_list(request):
  posts = request.user.scrap_users.all()
  # scrap_post가 post를 fk로 갖고 있어서
  print(posts)
  #posts = Post.post_user.scrap_post.all()
  #posts = Post.scrap_post.filter(user = request.user)
  return render(request, 'accounts/scrap_list.html', {'posts': posts})