from .models import Articles, Profile, Lesson, StudentsGroup, Document, Deadlines
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
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/mains/")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def home(request):
    return render(request, 'pages/home.html')


@login_required(login_url='login/')
def core(request):
    list_articles = Articles.objects.all()
    context = {
        'list_articles': list_articles
    }
    template = 'core/core.html'
    return render(request, template, context)


@login_required(login_url='login/')
def detail(request, id):
    get_articles = Articles.objects.get(id=id)
    context = {
        'get_articles': get_articles
    }
    template = 'core/detail.html'
    return render(request, template, context)


class user_logout(LogoutView):
    next_page = reverse_lazy('core')
    
@login_required(login_url='login/')
def lessons(request):
    get_profile = Profile.objects.get(id=request.user.id)
    get_group = StudentsGroup.objects.all()
    get_lessons = Lesson.objects.all()
    get_document = Document.objects.all()
    get_deadlines = Deadlines.objects.all().filter(groups_id=get_profile.student_group.id)
    context = {
        'get_lesson': get_lessons,
        'get_group': get_group,
        'get_profile': get_profile,
        'get_file': get_document,
        'get_deadlines': get_deadlines,
    }
    template = 'core/lessons.html'
    return render(request, template, context)


@login_required(login_url='login/')
def lesson(request, id):
    get_lessons = Lesson.objects.get(id=id)
    context = {
        'get_lesson': get_lessons,
    }
    template = 'core/lesson.html'
    return render(request, template, context)


@login_required(login_url='login/')
def profile(request):
    get_user = User.objects.get(id=request.user.id)
    context = {
        'get_user': get_user
    }
    template = 'accounts/profile.html'
    return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect('login/')


def redir(request):
    return redirect('login/')
