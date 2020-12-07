# Generated by Django 3.1.3 on 2020-12-07 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles_data', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='article')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=20)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentsGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('lessons', models.ManyToManyField(blank=True, to='core.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subgroup', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Both', 'Both')], max_length=6)),
                ('week_day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=9)),
                ('time', models.IntegerField()),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.studentsgroup')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_permission', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Admin', 'Admin')], default='Student', max_length=7)),
                ('github', models.CharField(blank=True, max_length=30)),
                ('numberphone', models.CharField(blank=True, max_length=13)),
                ('img', models.ImageField(blank=True, upload_to='profile_img')),
                ('student_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.studentsgroup')),
                ('teacher_lesson', models.ManyToManyField(blank=True, to='core.Lesson')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deadlines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('deadline_time', models.DateTimeField(blank=True)),
                ('files', models.ManyToManyField(blank=True, to='core.Document')),
                ('groups', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.studentsgroup')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=30)),
                ('document', models.FileField(blank=True, upload_to='document/')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lesson')),
            ],
        ),
    ]
