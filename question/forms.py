from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board # Board 와 연결
        fields = ['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] #author 
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 80})
        }

        def save(self, commit=True):
            comment = Comment(**self.cleaned_data)
            if commit:
                comment.save()
            return comment 
    