from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        # this is the default widget: a single line textbox
        # widgets={'text':forms.TextInput()}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Please type in contents:'}
        widgets = {'text': forms.Textarea(attrs={'col': 80})}
