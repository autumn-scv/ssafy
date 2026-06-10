from django import forms
from .models import Todo, Comment


class TodoForm(forms.ModelForm):
  class Meta:
    model = Todo
    fields = ('title', 'content', 'image')

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('content',)
