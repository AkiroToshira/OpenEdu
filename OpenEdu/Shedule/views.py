from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Profile, Schedule, StudentGroupLesson


def schedule_by_day(schedule):
    schedule_monday = schedule[0]
    schedule_tuesday = schedule[1]
    schedule_wednesday = schedule[2]
    schedule_thursday = schedule[3]
    schedule_friday = schedule[4]
    return schedule_monday, schedule_tuesday, schedule_wednesday, schedule_thursday, schedule_friday


@login_required(login_url='/login')
def schedule(request):
    get_profile = Profile.objects.get(id=request.user.id)
    group = get_profile.get_student_group()
    schedule = group.get_shedule()
    schedule_monday, schedule_tuesday, schedule_wednesday, schedule_thursday, schedule_friday = \
        schedule_by_day(schedule)
    context = {
        'schedule_monday': schedule_monday,
        'schedule_tuesday': schedule_tuesday,
        'schedule_wednesday': schedule_wednesday,
        'schedule_thursday': schedule_thursday,
        'schedule_friday': schedule_friday,
    }
    template = 'Shedule/shedule.html'
    return render(request, template, context)


@login_required(login_url='/login')
def schedulet(request):
    get_profile = Profile.objects.get(id=request.user.id)
    schedule=get_profile.get_teacher_schedule()
    schedule_monday, schedule_tuesday, schedule_wednesday, schedule_thursday, schedule_friday = \
        schedule_by_day(schedule)
    context = {
        'schedule_monday': schedule_monday,
        'schedule_tuesday': schedule_tuesday,
        'schedule_wednesday': schedule_wednesday,
        'schedule_thursday': schedule_thursday,
        'schedule_friday': schedule_friday,
    }
    template = 'Shedule/shedule.html'
    return render(request, template, context)