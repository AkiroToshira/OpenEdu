from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DeadLinesForm, ChapterForm, EditDeadLinesForm
from core.models import Deadlines, Lesson, Profile, Chapter, StudentGroupLesson, Group


@login_required(login_url='/login')
def lessonst(request):
    if request.method == 'POST':
        form = DeadLinesForm(request.POST)
        if form.is_valid():
            new_deadlines = Deadlines()
            new_deadlines.name = form.cleaned_data['name']
            new_deadlines.deadline_time = form.cleaned_data['deadline_time']
            new_deadlines.student_group_lesson = StudentGroupLesson.objects.get(
                lesson=Lesson.objects.get(id=form.cleaned_data['lesson']))
            new_deadlines.save()
            return redirect('/lessonst/')
    get_profile = Profile.objects.get(id=request.user.id)
    get_lessons = get_profile.get_teacher_lessons()
    get_deadlines = get_profile.get_deadlines().order_by('deadline_time')
    groups = StudentGroupLesson.objects.all().filter(lesson__in=get_lessons).distinct()
    form = DeadLinesForm()
    context = {
        'get_lesson': get_lessons,
        'get_profile': get_profile,
        'get_deadlines': get_deadlines,
        'form': form,
        'get_group': groups,
    }
    template = 'TeacherLessons/classest.html'
    return render(request, template, context)


def editdeadline(request, id):
    update_deadline = Deadlines.objects.get(id=id)
    if request.method == 'POST':
        form = EditDeadLinesForm(request.POST, request.FILES)
        if form.is_valid():
            update_deadline.name = form.cleaned_data['name']
            update_deadline.deadline_time = form.cleaned_data['deadline_time']
            update_deadline.lesson_group = StudentGroupLesson.objects.get(id=form.cleaned_data['lesson'])
            update_deadline.save()
            return redirect('/lessonst/')
    get_profile = Profile.objects.get(id=request.user.id)
    teacher_lessons = get_profile.get_teacher_lessons()
    lessons = StudentGroupLesson.objects.all().filter(lesson__in=teacher_lessons).order_by('lesson')
    context = {
        'get_lesson': lessons,
        'update_deadline': update_deadline,
    }
    template = 'TeacherLessons/editdeadlines.html'
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
    get_group = StudentGroupLesson.objects.all().filter(lesson=id)
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


def deletechapter(request, id):
    delete_chapter = Chapter.objects.get(id=id)
    current_lesson_id = delete_chapter.lesson_id
    Chapter.objects.get(id=id).delete()
    return redirect('/lessonst/lesson/' + str(current_lesson_id))


def deletedeadlines(requset, id):
    Deadlines.objects.get(id=id).delete()
    return redirect('/lessonst/')
