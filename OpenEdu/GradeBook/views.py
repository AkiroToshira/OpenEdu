from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import GradeBook, BookColumn


@login_required(login_url='/login')
def gradebookteacher(request, id):
    get_columns = BookColumn.objects.all().filter(gradebook=id)
    book = GradeBook.objects.get(id=id)
    context = {
        'get_columns': get_columns,
        'get_check': book.get_grades(),
    }
    template = 'GradeBook/diary.html'
    return render(request, template, context)


@login_required(login_url='/login')
def gradebookhub(request):
    template = 'core/diary.html'
    return render(request, template)


def gradebookstudent(request):
    pass


def gradebook(request):
    pass