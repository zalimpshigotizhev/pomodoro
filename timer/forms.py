from django import forms
import core


class UploadFileForm(forms.Form):
    file = forms.FileField()

class ColorConfigForm(forms.Form):
    color = forms.CharField()

class CreateTaskForms(forms.Form):
    name = forms.CharField(label='Название задачи', max_length=core.MAX_LENGTH_NAME_THEME)
    name.widget.attrs.update({"class": "input-name-tasks"})

    def clean_name(self):
        name = self.cleaned_data['name']
        return name