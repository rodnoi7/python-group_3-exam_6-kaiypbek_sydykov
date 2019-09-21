from django.shortcuts import render, redirect, get_object_or_404
from guest_book.models import Record
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index_view(request):
    if request.GET.get('author'):
        records = Record.objects.filter(headline__author=request.GET.get('author'))
        context = {
            'records': records
        }
        return render(request, 'index.html', context)
    else:
        records = Record.objects.filter(status='Active').order_by('-created_at')
        context = {
            'records': records
        }
        return render(request, 'index.html', context)

def create_view(request):
    if request.method == 'GET':
        return render(request, 'add_article.html')
    elif request.method == 'POST':
        author = request.POST.get('author')
        author_email = request.POST.get('author_email')
        text = request.POST.get('text')
        article = Record.objects.create(author=author, author_email=author_email, text=text)
        return redirect('index')

def delete_view(request, record_pk):
    if (request.method == 'GET'):
        record = get_object_or_404(Record, pk=record_pk)
        context = {
            'record': record
        }
        return render(request, 'delete.html', context)
    elif(request.method == 'POST'):
        if request.POST.get('answer') == 'yes':
            record = Record.objects.get(pk=record_pk)
            record.delete()
            return redirect('index')
        else:
            return redirect('index')

def update_view(request, record_pk):
    try:
        record = Record.objects.get(pk=record_pk)
    except User.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        context = {
            'record': record
        }
        return render(request, 'update.html', context)
    elif request.method == 'POST':
        record.author = request.POST.get('author')
        record.author_email = request.POST.get('author_email')
        record.text = request.POST.get('text')
        record.save()
        return redirect('index')