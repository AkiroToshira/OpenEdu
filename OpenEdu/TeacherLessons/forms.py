from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class DeadLinesForm(forms.Form):
    name = forms.CharField(max_length=20)
    deadline_time = forms.DateField(widget=DateInput)
    lesson = forms.IntegerField(required=True)


class ChapterForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(required=False, widget=forms.Textarea())
    document = forms.FileField(required=False)