# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Column, Article


def index(request):
    return HttpResponse(u'欢迎来自强学堂学习Django')

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})
    # return HttpResponse('column slug: ' + column_slug)

def article_detail(request, article_slug):
    article = Article.objects.filter(slug=article_slug)[0]
    return render(request, 'news/article.html', {'article': article})
    # return HttpResponse('article slug: ' + article_slug)

def index(request):
    columns = Column.objects.all()
    return render(request, 'index.html', {'columns': columns})