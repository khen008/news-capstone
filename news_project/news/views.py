from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer


# Homepage
def home(request):

    articles = Article.objects.all().order_by("-created_at")

    return render(request, "news/home.html", {"articles": articles})


# Article page
def article_detail(request, pk):

    article = get_object_or_404(Article, pk=pk)

    return render(request, "news/article_detail.html", {"article": article})


# API - list and create
class ArticleListCreateView(generics.ListCreateAPIView):

    queryset = Article.objects.all()

    serializer_class = ArticleSerializer


# API - detail update delete
class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()

    serializer_class = ArticleSerializer