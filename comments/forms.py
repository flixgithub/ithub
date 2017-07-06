from .models import Comment
from django import forms

# -*- coding:utf8 -*-


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
