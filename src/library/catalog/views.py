from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}.")
                return redirect("catalog:index")
            else:
                messages.error(request,"Invalid username or passowrd.")
        else:
            messages.error(request,"Invalid username or password.")
    form =AuthenticationForm()
    return render(request=request, template_name="login.html",context={"login_form":form})