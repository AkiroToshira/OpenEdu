from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Profile, Schedule


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
    template = 'Shedule/shedule.html'
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
    template = 'Shedule/shedule.html'
    return render(request, template, context)