from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Category, Article
from .forms import *

def index(request, slug=None):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    if not slug:
        articles = Article.objects.all()
    else:
        category = get_object_or_404(Category, slug=slug)
        articles = Article.objects.filter(category=category)
    context = {**context, 'articles': articles}
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def add_article(request):
    return render(request, 'add_article.html')


def article_details(request, article_id=None, slug=None):
    article = get_object_or_404(Article, pk=article_id, slug=slug)
    categories = Category.objects.all()
    context = {
        'article': article,
        'categories': categories
    }
    return render(request, 'article_details.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{'form': form})

def user_logout(request):
    logout(request)
    return redirect('/login')