from django.shortcuts import render, redirect, get_object_or_404
from guest_book.models import Article
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index_view(request):
    if request.GET.get('author'):
        articles = Article.objects.filter(Arauthor=request.GET.get('author').lower())
        context = {
            'articles': articles
        }
        return render(request, 'index.html', context)
    else:
        articles = Article.objects.filter(status='Active').order_by('-created_at')
        context = {
            'articles': articles
        }
        return render(request, 'index.html', context)

def create_view(request):
    if request.method == 'GET':
        return render(request, 'add_article.html')
    elif request.method == 'POST':
        author = request.POST.get('author')
        author_email = request.POST.get('author_email')
        text = request.POST.get('text')
        article = Article.objects.create(author=author, author_email=author_email, text=text)
        return redirect('index')

def delete_view(request, article_pk):
    if (request.method == 'GET'):
        article = get_object_or_404(Article, pk=article_pk)
        context = {
            'article': article
        }
        return render(request, 'delete.html', context)
    elif(request.method == 'POST'):
        if request.POST.get('answer') == 'yes':
            article = Article.objects.get(pk=article_pk)
            article.delete()
            return redirect('index')
        else:
            return redirect('index')

def update_view(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
    except User.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        context = {
            'article': article
        }
        return render(request, 'update.html', context)
    elif request.method == 'POST':
        article.author = request.POST.get('author')
        article.author_email = request.POST.get('author_email')
        article.text = request.POST.get('text')
        article.save()
        return redirect('index')