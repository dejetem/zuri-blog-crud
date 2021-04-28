from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'put your title here'}),
            'author':forms.Select(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'type your message here'}),
        }