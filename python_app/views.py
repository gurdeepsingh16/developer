from django.shortcuts import render, redirect
from .models import *
from python_app.forms import tut_form, Sub_topic, practice_form
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.

# paginator and data show and form


@login_required(login_url='login')
@never_cache
def home(request):
    if request.user.is_authenticated:
        data = tut.objects.all()
        paginator = Paginator(data, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'home.html', {'data': page_obj})
    else:
        return render(request, 'home.html',)


def show_practice(request):
    data = practice_set.objects.all()
    return render(request, 'show_practice_set.html', {'data': data})


def practice_more(request, id):
    data = practice_set.objects.get(id=id)
    return render(request, 'show_practice_set.html', {'data1': data})


@login_required(login_url='login')
def add_func(request):
    if request.method == 'GET':
        form = tut_form
        return render(request, 'add.html', {'form': form})

    else:
        form = tut_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'add.html')


# add practice set
@login_required(login_url='login')
def add_pracctice(request):
    if request.method == 'GET':
        form = practice_form
        return render(request, 'add.html', {'form': form})

    else:
        form = practice_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render(request, 'add.html')
# searching


@login_required(login_url='login')
def search(request):
    try:
        searchinp = request.POST['search']
        data = tut.objects.filter(title__contains=searchinp)
        return render(request, 'searching.html', {'data1': data})

    except:
        return render(request, 'searching.html')


@login_required(login_url='login')
def search_subtopic(request):
    data = Sub_topic.objects.all()
    return render(request, 'sample.html', {'data': data})


@login_required(login_url='login')
def search_subtopic2(request, id):
    data1 = Sub_topic.objects.get(id=id)
    data = tut.objects.filter(sub_topic__exact=data1)
    return render(request, 'sample.html', {'data1': data})

# login and register and logout


# def register(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         if password == confirm_password:

#             data = User.objects.create_user(
#                 username=username, email=email, password=password)
#             data.save()
#             return redirect('home')

#     return render(request, 'register.html')


# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return redirect('login')

#     return render(request, 'login.html')


# @never_cache
# def logout(request):
#     auth.logout(request)
#     return redirect('login')
