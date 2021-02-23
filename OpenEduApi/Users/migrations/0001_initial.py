# Generated by Django 3.1.5 on 2021-02-15 21:43

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
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('year', models.PositiveIntegerField(default=1)),
                ('curator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='curatorial_group', to=settings.AUTH_USER_MODEL)),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.department')),
                ('student', models.ManyToManyField(blank=True, related_name='Student_group', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=150)),
                ('account_permission', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Admin', 'Admin')], default='Student', max_length=7)),
                ('numberphone', models.CharField(blank=True, max_length=13)),
                ('credit_book_number', models.CharField(blank=True, max_length=8)),
                ('img', models.ImageField(blank=True, default='profile_img/profile_photo.jpg', upload_to='profile_img')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('year', models.PositiveIntegerField(default=1)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.group')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.institute')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.faculty'),
        ),
    ]
