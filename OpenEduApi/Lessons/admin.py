from django.contrib import admin

from .models import *

admin.site.register(Lesson)
admin.site.register(TeacherLesson)
admin.site.register(StudentGroupLesson)
admin.site.register(Chapter)
admin.site.register(Document)

