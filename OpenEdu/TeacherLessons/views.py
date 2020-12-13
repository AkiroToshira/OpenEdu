from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DeadLinesForm, ChapterForm
from core.models import Deadlines, Lesson, StudentsGroup, Profile, Chapter


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
    template = 'TeacherLessons/classest.html'
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
    template = 'TeacherLessons/lessont.html'
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
            return redirect('/lessonst/lesson/' + str(current_lesson_id))
    form = ChapterForm(initial={'name': get_chapter.name,
                                'description': get_chapter.description,
                                'document': get_chapter.document})
    context = {
        'get_chapter': get_chapter,
        'form': form
    }
    template = 'TeacherLessons/editchapter.html'
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
    template = 'TeacherLessons/editdeadlines.html'
    return render(request, template, context)


def deletechapter(request, id):
    print('------------------------------------------------')
    print(id)
    delete_chapter = Chapter.objects.get(id=id)
    current_lesson_id = delete_chapter.lesson_id
    Chapter.objects.get(id=id).delete()
    return redirect('/lessonst/lesson/' + str(current_lesson_id))


def deletedeadlines(requset, id):
    Deadlines.objects.get(id=id).delete()
    return redirect('/lessonst/')
