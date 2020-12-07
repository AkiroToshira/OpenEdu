from .models import Articles, Profile, Lesson, Deadlines, Schedule, Chapter, StudentsGroup
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, ChapterForm, DeadLinesForm
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
                    return HttpResponseRedirect("/mains/")
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
def lessons(request):
    get_profile = Profile.objects.get(id=request.user.id)
    get_lessons = get_profile.student_group.lessons.all()
    get_deadlines = Deadlines.objects.all().filter(groups_id=get_profile.student_group.id)
    context = {
        'get_lesson': get_lessons,
        'get_deadlines': get_deadlines,
        'get_profile': get_profile,
    }
    template = 'core/classes.html'
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
    print(get_lessons)
    print(schedule_monday)
    template = 'core/shedule.html'
    return render(request, template, context)


@login_required(login_url='/login')
def lesson(request, id):
    get_lessons = Lesson.objects.get(id=id)
    get_chapter = Chapter.objects.all().filter(lesson=id)
    context = {
        'get_lesson': get_lessons,
        'get_chapter': get_chapter,
    }
    template = 'core/class.html'
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


@login_required(login_url='/login')
def lessonst(request):
    get_profile = Profile.objects.get(id=request.user.id)
    get_lessons = get_profile.teacher_lesson.all()
    get_deadlines = Deadlines.objects.all().filter(lesson__in=get_lessons)
    context = {
        'get_lesson': get_lessons,
        'get_profile': get_profile,
        'get_deadlines': get_deadlines,
    }
    template = 'core/classest.html'
    return render(request, template, context)


@login_required(login_url='/login')
def lessont(request, id):
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            new_chapter = Chapter.objects.create(lesson_id=id)
            new_chapter.name = form.cleaned_data['name']
            new_chapter.description = form.cleaned_data['description']
            new_chapter.document = form.cleaned_data['document']
            new_chapter.save()
            return redirect('/lessont/lesson/<int:id>')
    get_lessons = Lesson.objects.get(id=id)
    get_chapter = Chapter.objects.all().filter(lesson=id)
    get_group = StudentsGroup.objects.all().filter(lessons=id)
    form = ChapterForm()
    refactor = False
    refactor_id = 0
    context = {
        'get_lesson': get_lessons,
        'get_chapter': get_chapter,
        'get_group': get_group,
        'form': form,
        'refactor': refactor,
        'refactor_id': refactor_id,
    }
    template = 'core/lessont.html'
    return render(request, template, context)


def addchapter(request, id):
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            new_chapter = Chapter.objects.create(lesson_id=id)
            new_chapter.name = form.cleaned_data['name']
            new_chapter.description = form.cleaned_data['description']
            new_chapter.document = form.cleaned_data['document']
            print(new_chapter)
            new_chapter.save()
            return redirect('/lessont/lesson/',1)
    else:
        form = ChapterForm()
    context = {
        'form': form,
    }
    template = 'core/addchapter.html'
    return render(request, template, context)


def deletechapter(request, id):
    Chapter.objects.get(id=id).delete()
    print(id)
    return redirect('/lessont/lesson/')
