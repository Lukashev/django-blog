from django.shortcuts import render, get_object_or_404
from .models import Category, Article


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