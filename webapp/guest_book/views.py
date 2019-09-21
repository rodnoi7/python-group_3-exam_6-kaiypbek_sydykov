from django.shortcuts import render, redirect, get_object_or_404
from guest_book.models import Article
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index_view(request):
	articles = Article.objects.filter(status='Active').order_by('-created_at')
	context = {
		'articles': articles
	}
	return render(request, 'index.html', context)
