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
    list_articles = Articles.objects.all()
    context = {
        'list_articles': list_articles
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
def schedule(request):
    get_profile = Profile.objects.get(id=request.user.id)
    schedule_monday = Schedule.objects.all().filter(group_id=get_profile.student_group.id, week_day='Monday')
    schedule_tuesday = Schedule.objects.all().filter(group_id=get_profile.student_group.id, week_day='Tuesday')
    schedule_wednesday = Schedule.objects.all().filter(group_id=get_profile.student_group.id, week_day='Wednesday')
    schedule_thursday = Schedule.objects.all().filter(group_id=get_profile.student_group.id, week_day='Thursday')
    schedule_friday = Schedule.objects.all().filter(group_id=get_profile.student_group.id, week_day='Friday')
    context = {
        'schedule_monday': schedule_monday,
        'schedule_tuesday': schedule_tuesday,
        'schedule_wednesday': schedule_wednesday,
        'schedule_thursday': schedule_thursday,
        'schedule_friday': schedule_friday,
    }
    template = 'core/shedule.html'
    return render(request, template, context)


@login_required(login_url='/login')
def schedulet(request):
    get_profile = Profile.objects.get(id=request.user.id)
    get_lessons = get_profile.teacher_lesson.all()
    schedule_monday = Schedule.objects.all().filter(lesson_id__in=get_lessons, week_day='Monday')
    schedule_tuesday = Schedule.objects.all().filter(lesson_id__in=get_lessons, week_day='Tuesday')
    schedule_wednesday = Schedule.objects.all().filter(lesson_id__in=get_lessons, week_day='Wednesday')
    schedule_thursday = Schedule.objects.all().filter(lesson_id__in=get_lessons, week_day='Thursday')
    schedule_friday = Schedule.objects.all().filter(lesson_id__in=get_lessons, week_day='Friday')
    context = {
        'schedule_monday': schedule_monday,
        'schedule_tuesday': schedule_tuesday,
        'schedule_wednesday': schedule_wednesday,
        'schedule_thursday': schedule_thursday,
        'schedule_friday': schedule_friday,
    }
    template = 'core/shedule.html'
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


def gradebook(request, id):
    get_columns = BookColumn.objects.all().filter(gradebook=id)
    book = GradeBook.objects.get(id=id)
    context = {
        'get_columns': get_columns,
        'get_check': book.get_grades(),
    }
    template = 'core/diary.html'
    return render(request, template, context)


def gradebookhub(request):
    template = 'core/diary.html'
    return render(request, template)