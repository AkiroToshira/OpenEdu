from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import GradeBook, BookColumn, Profile, Lesson


@login_required(login_url='/login')
def gradebookteacher(request, id):
    get_columns = BookColumn.objects.all().filter(gradebook=id)
    book = GradeBook.objects.get(id=id)
    data = []
    i = 0
    for colum in book.get_grades():
        data.append([])
        for grade in colum:
            data[i].append({"date": str(grade.date.date), "grades": str(grade.value), "student": str(grade.user)})
        i = i + 1

    context = {
        'get_columns': get_columns,
        'get_check': book.get_grades(),
        'raw_data': data,
    }
    template = 'GradeBook/diary.html'
    return render(request, template, context)


@login_required(login_url='/login')
def gradebookhub(request):
    template = 'GradeBook/diary_hub.html'
    return render(request, template)


def gradebookstudent(request):
    class LessonGrade:
        grades = []
        lesson = Lesson

    get_profile = Profile.objects.get(id=request.user.id)
    grade = get_profile.get_grades()
    grades = []
    for i in grade:
        tmp = LessonGrade()
        tmp.grades = grade[i]
        tmp.lesson = i
        grades.append(tmp)
    context = {
        'grades': grades,
    }
    template = 'GradeBook/student_diary.html'
    return render(request, template, context)


def gradebook(request):
    pass
