from django.contrib import admin

from .models import *

admin.site.register(GradeBook)
admin.site.register(BookColumn)
admin.site.register(Grade)
admin.site.register(ExamGrade)

