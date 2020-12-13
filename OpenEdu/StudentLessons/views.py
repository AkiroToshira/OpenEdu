from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Profile, Deadlines, Lesson, Chapter



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
    template = 'StudentLessons/classes.html'
    return render(request, template, context)


@login_required(login_url='/login')
def lesson(request, id):
    get_lessons = Lesson.objects.get(id=id)
    get_chapter = Chapter.objects.all().filter(lesson=id)
    context = {
        'get_lesson': get_lessons,
        'get_chapter': get_chapter,
    }
    template = 'StudentLessons/class.html'
    return render(request, template, context)