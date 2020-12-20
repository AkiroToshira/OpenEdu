from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})


@login_required(login_url='/login')
def core(request):
    list_articles = Articles.objects.all().filter(is_main=False)
    main_article = Articles.objects.get(is_main=True)
    context = {
        'list_articles': list_articles,
        'main_article': main_article,
    }
    template = 'core/news.html'
    return render(request, template, context)


@login_required(login_url='/login')
def detail(request, id):
    get_articles = Articles.objects.get(id=id)
    context = {
        'get_articles': get_articles
    }
    template = 'core/detail.html'
    return render(request, template, context)


@login_required(login_url='/login')
def profile(request):
    get_user = User.objects.get(id=request.user.id)
    context = {
        'get_user': get_user
    }
    template = 'core/profile.html'
    return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect('/login')


def redir(request):
    return redirect('/login')