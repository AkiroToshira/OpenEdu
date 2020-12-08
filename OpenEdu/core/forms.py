from django import forms


class ChapterForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(required=False, widget=forms.Textarea())
    document = forms.FileField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DateInput(forms.DateInput):
    input_type = 'date'


class DeadLinesForm(forms.Form):
    name = forms.CharField(max_length=20)
    deadline_time = forms.DateField(widget=DateInput)
    lesson = forms.IntegerField(required=True)
    group = forms.IntegerField(required=True)
    is_edit = forms.BooleanField(required=False)
