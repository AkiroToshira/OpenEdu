from django.contrib import admin
from .models import *

admin.site.site_header = "Administration"
admin.site.site_title = "Administration"
admin.site.index_title = "Home"
admin.site.site_url = None

admin.site.register(Articles)
admin.site.register(Lesson)
admin.site.register(Profile)
admin.site.register(Schedule)
admin.site.register(Chapter)
admin.site.register(Document)
admin.site.register(Group)
admin.site.register(StudentGroup)
admin.site.register(GradeBook)
admin.site.register(StudentGroupLesson)
admin.site.register(BookColumn)
admin.site.register(Grade)
admin.site.register(Institute)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Deadlines)
admin.site.register(TeacherLesson)



