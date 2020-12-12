from .models import *
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
    if request.method == 'POST':
        form = DeadLinesForm(request.POST)
        if form.is_valid():
            new_deadlines = Deadlines()
            new_deadlines.name = form.cleaned_data['name']
            new_deadlines.deadline_time = form.cleaned_data['deadline_time']
            new_deadlines.lesson = Lesson.objects.get(id=form.cleaned_data['lesson'])
            new_deadlines.groups = StudentsGroup.objects.get(id=form.cleaned_data['group'])
            new_deadlines.save()
            print(new_deadlines)
            return redirect('/lessonst/')
    get_profile = Profile.objects.get(id=request.user.id)
    get_lessons = get_profile.teacher_lesson.all()
    get_deadlines = Deadlines.objects.all().filter(lesson__in=get_lessons).order_by('deadline_time')
    get_group = StudentsGroup.objects.all().filter(lessons__in=get_lessons).distinct()
    form = DeadLinesForm()
    context = {
        'get_lesson': get_lessons,
        'get_profile': get_profile,
        'get_deadlines': get_deadlines,
        'form': form,
        'get_group': get_group,
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
            #return redirect('/lessont/lesson/<int:id>')
            return redirect('/lessonst/lesson/' + str(id))
    get_lessons = Lesson.objects.get(id=id)
    get_chapter = Chapter.objects.all().filter(lesson=id)
    get_group = StudentsGroup.objects.all().filter(lessons=id)
    form = ChapterForm()
    context = {
        'get_lesson': get_lessons,
        'get_chapter': get_chapter,
        'get_group': get_group,
        'form': form,
    }
    template = 'core/lessont.html'
    return render(request, template, context)


def editchapter(request, id):
    get_chapter = Chapter.objects.get(id=id)
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            update_chapter = Chapter.objects.get(id=id)
            current_lesson_id = update_chapter.lesson_id
            update_chapter.name = form.cleaned_data['name']
            update_chapter.description = form.cleaned_data['description']
            if form.cleaned_data['document'] != None:
                update_chapter.document = form.cleaned_data['document']
            else:
                update_chapter.document = get_chapter.document
            update_chapter.save()
            #return redirect('../../')
            return redirect('/lessonst/lesson/' + str(current_lesson_id))
    form = ChapterForm(initial={'name': get_chapter.name,
                                'description': get_chapter.description,
                                'document': get_chapter.document})
    context = {
        'get_chapter': get_chapter,
        'form': form
    }
    template = 'core/editchapter.html'
    return render(request, template, context)


def editdeadline(request, id):
    update_deadline = Deadlines.objects.get(id=id)
    if request.method == 'POST':
        form = DeadLinesForm(request.POST, request.FILES)
        if form.is_valid():
            update_deadline.name = form.cleaned_data['name']
            update_deadline.deadline_time = form.cleaned_data['deadline_time']
            update_deadline.lesson = Lesson.objects.get(id=form.cleaned_data['lesson'])
            update_deadline.groups = StudentsGroup.objects.get(id=form.cleaned_data['group'])
            print(form)
            update_deadline.save()
            return redirect('/lessonst/')
    get_profile = Profile.objects.get(id=request.user.id)
    get_lesson = get_profile.teacher_lesson.all()
    get_group = StudentsGroup.objects.all().filter(lessons__in=get_lesson).distinct()
    form = ChapterForm()
    context = {
        'form': form,
        'get_lesson': get_lesson,
        'get_group': get_group,
        'update_deadline': update_deadline,
    }
    template = 'core/editdeadlines.html'
    return render(request, template, context)


def deletechapter(request, id):
    delete_chapter = Chapter.objects.get(id=id)
    current_lesson_id = delete_chapter.lesson_id
    Chapter.objects.get(id=id).delete()
    #return redirect('/lessont/lesson/')
    return redirect('/lessonst/lesson/' + str(current_lesson_id))


def deletedeadlines(requset, id):
    Deadlines.objects.get(id=id).delete()
    return redirect('/lessonst/')


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