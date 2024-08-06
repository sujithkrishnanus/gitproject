from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book
from .forms import AuthorForm,BookForm

# Create your views here.

def listView(request):
    books=Book.objects.all()

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'admn/listbook.html',{'books':books,'page':page})

def detailsBook(request,book_id):
    book=Book.objects.get(id=book_id)

    return render(request,'admn/detail.html',{'book':book})

def deleteBook(request,book_id):
    book=Book.objects.get(id=book_id)

    if request.method=="POST":
        book.delete()
        return redirect('/')

    return render(request,'admn/delete.html',{'book':book})

def createBook(request):
    books=Book.objects.all()

    if request.method=='POST':
        form=BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    else:
        form=BookForm

    return render(request,'admn/book.html',{'form':form,'books':books})


def CreateAuthor(request):
    if request.method=='POST':
        form=AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form=AuthorForm

    return render(request,'admn/author.html',{'form':form})

def updateBook(request,book_id):
    book=Book.objects.get(id=book_id)

    if request.method=='POST':
        form=BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form=BookForm(instance=book)

    return render(request,'admn/update.html',{'form':form})

def index(request):
    return render(request,'admn/base.html')

def searchBook(request):

    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'admn/searchbook.html',context)









