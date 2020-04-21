from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Book.models import Book
from Book.forms import BookForm, CreateUserForm
from django.contrib import messages
from Book.decorators import admin_only


@login_required(login_url='login')
def homePage(request):

    books = Book.objects.all()
    context = {'books': books}

    return render(request, 'Book/homePage.html', context)


@login_required(login_url='login')
def UploadBook(request):

    bookform = BookForm()
    context = {'bookform': bookform, }
    if request.method == 'POST':
        bookform = BookForm(request.POST, request.FILES)
        if bookform.is_valid():
            bookform.save()
            return redirect('/')
        else:
            return render(request, 'Book/book.html', context)
    return render(request, 'Book/book.html', context)


@login_required(login_url='login')
def EditBook(request, pk):
    try:
        bookform = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return redirect('homePage')
    bookform = BookForm(request.POST or None, instance=bookform)
    if bookform.is_valid():
        bookform.save()
        return redirect('homePage')
    return render(request, 'Book/book.html', {'bookform': bookform})


@login_required(login_url='login')
def DeleteBook(request, pk):
    try:
        book = Book.objects.get(id=pk)
        book.delete()
        return redirect('homePage')
    except Book.DoesNotExist:
        return redirect('homePage')


def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'Book/login.html', context)


def LogOut(request):

    logout(request)
    return redirect('login')


@login_required(login_url='login')
def RegisterPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'Book/register2.html', context)
