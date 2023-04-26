from django import forms
from django.contrib.auth.models import User # импортируем модель пользователя
from .models import Post # импортируем модель поста

class UserForm(forms.ModelForm):
    # форма регистации пользователя
    password = forms.CharField( widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email')

class PostForm(forms.ModelForm):
    # форма создания поста
    class Meta:
        model = Post
        fields = '__all__'