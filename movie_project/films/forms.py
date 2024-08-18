from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']
        labels = {
            'title': 'Название фильма',
            'description': 'Описание фильма',
            'review': 'Отзыв',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фильма'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание фильма',
                'rows': 3
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш отзыв',
                'rows': 5
            }),
        }
