from django.shortcuts import render
from .models import NewsCategory, Author, News

def home_page(request):
    categories = NewsCategory.objects.all()
    authors = Author.objects.all()
    news = News.objects.all()

    context = {
        'categories': categories,
        'authors': authors,
        'news': news,
    }
    return render(request, 'home.html', context)

def category_page(request, pk):
    category = NewsCategory.objects.filter(id=pk).first()
    news_list = News.objects.filter(category=category) if category else News.objects.none()

    context = {
        'category': category,
        'news_list': news_list,
    }
    return render(request, 'category.html', context)

def news_detail(request, pk):
    news_item = News.objects.filter(id=pk).first()

    context = {
        'news': news_item,
    }
    return render(request, 'news_detail.html', context)
