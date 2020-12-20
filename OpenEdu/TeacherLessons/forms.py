from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class DeadLinesForm(forms.Form):
    name = forms.CharField(max_length=20)
    deadline_time = forms.DateField(widget=DateInput)
    lesson = forms.IntegerField(required=True)


class EditDeadLinesForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    deadline_time = forms.DateField(widget=DateInput, required=False)
    lesson = forms.IntegerField(required=False)


class ChapterForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(required=False, widget=forms.Textarea())
    document = forms.FileField(required=False)