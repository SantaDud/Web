from django.shortcuts import render
from .models import Book, User
from random import randint
# Create your views here.

def index(request):
    numberOfBooks = Book.objects.count()
    first = Book.objects.first().pk
    bookIds = []
    for i in range(3):
        temp = randint(first, numberOfBooks + first - 1)
        while(temp in bookIds):
            temp = randint(first, numberOfBooks + first - 1)
        bookIds.append(temp)
    return render(request, 'libr/index.html', {
        "books": Book.objects.all(),
        "rBook1": Book.objects.get(pk = int(bookIds[1])),
        "rBook2": Book.objects.get(pk = int(bookIds[0])),
        "rBook3": Book.objects.get(pk = int(bookIds[2])),
    })

def book(request, book_id):
    return render(request, 'libr/book.html', {
        "book": Book.objects.get(pk = book_id)
    })

def search(request):
    searchText = request.GET['searchText']
    return render(request, 'libr/search.html', {
        "books": Book.objects.filter(title__icontains = searchText)
    })

def signup(request):
    return render(request, 'libr/signup.html')

def registered(request):
    User.objects.create(
        fname = request.POST['fname'],
        lname = request.POST['lname'],
        username = request.POST['username'],
        email = request.POST['email'],
        password = request.POST['password']
    )
    return render(request, 'libr/index.html', {
        "books": Book.objects.all()
    })