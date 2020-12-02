from django import forms


class ChapterForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(required=False, widget=forms.Textarea())
    document = forms.FileField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DeadLinesForm(forms.Form):
    name = forms.CharField(max_length=20)
    deadline_time = forms.DateTimeField()
    lesson = ['lessons']
    groups = ['groups']
