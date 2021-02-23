from django.db import models
from django.contrib.auth.models import User
from Users.models import Group


class Lesson(models.Model):
    """"Предмет"""
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30, blank=True)
    lesson_moderator = models.ManyToManyField(User, related_name='LessonModerator', blank=True)

    def __str__(self):
        return self.name


class LessonTeacher(models.Model):
    TYPE_CHOICE = (
        ('Lessons', 'L'),


        ('Practical ', 'P')
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='TeacherLesson')


class StudentGroupLesson(models.Model):
    """"Групи і викладачі прив'язані до предмету"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='GroupLesson', on_delete=models.CASCADE)
    teachers = models.ManyToManyField(LessonTeacher, related_name='StudentGroup')

    @classmethod
    def get_user_lesson(cls, user):
        if user.profile.account_permission == 'Student':
            group = Group.objects.get(student=user)
            lessons = StudentGroupLesson.objects.all().filter(group=group)
        elif user.profile.account_permission == 'Teacher':
            teacher_lessons = LessonTeacher.objects.all().filter(teacher=user)
            lessons = StudentGroupLesson.objects.all().filter(teachers__in=teacher_lessons)
        return lessons

    def get_lesson(self):
        return self.lesson.name

    def __str__(self):
        return "{} | {}".format(self.lesson.name, self.group.name)


class Lecture(models.Model):
    """Лекції які йдуть разом"""
    lesson = models.ManyToManyField(StudentGroupLesson, related_name='Lecture')


class Chapter(models.Model):
    """"Поділ розділів предмету"""
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30, blank=True)
    lesson = models.ForeignKey(Lesson, related_name='chapters', on_delete=models.CASCADE)


class Document(models.Model):
    """"Файли прикріплені до певного розділу"""
    chapter = models.ForeignKey(Chapter, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
