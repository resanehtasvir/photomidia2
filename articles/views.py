from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.
def articles(request):
    articles = models.Article.objects.all().order_by('date')
    args = {'articles':articles}
    return render(request, 'articles/articles.html', args)
def articles_detail(request, slug):
    article = models.Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article} )
