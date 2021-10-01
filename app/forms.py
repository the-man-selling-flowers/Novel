from typing import ContextManager
from django import forms
from django.db.models.query import FlatValuesListIterable
from .models import Category


class PostForm(forms.Form):
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category

    title = forms.CharField(max_length=30, label='タイトル')
    category = forms.ChoiceField(
        label='カテゴリー', widget=forms.Select, choices=list(category_choice.items()))
    content = forms.CharField(label='内容', widget=forms.Textarea)
    image = forms.ImageField(label='イメージ画像', required=False)
