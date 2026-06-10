# django
from django import forms
from .models import Article



# class ArticleForm(forms.Form):
#     title = rorms,forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta: 
        model = Article
        # fields = ['title', 'content'] # 사용자의 입력으로 받을 필드를 설정
        fields = '__all__' #전체 필드를 입력으로 받을 때 사용하는 설정