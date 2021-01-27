from django.contrib import admin

from .models import QuestionSet, Question, Answer, UserAnswer

admin.site.register(QuestionSet)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserAnswer)
