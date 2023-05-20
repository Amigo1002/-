"""
Definition of forms.
"""
from django.db import models
from .models import Comment
from .models import Blog

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    job = forms.CharField(label='Ваш род занятий', min_length=2, max_length=100)
    gender = forms.ChoiceField(label= 'Ваш пол',
                               choices=[('1', 'Мужской'), ('2', 'Женский')],
                               widget=forms.RadioSelect, initial=1)
    
    notice = forms.BooleanField(label='Получать новости сайта на e-mail?',
                                required=False)
    email = forms.EmailField(label='Ваш e-mail')
    message = forms.CharField(label='Коротко о себе', 
                              widget=forms.Textarea(attrs={'rows':12, 'cols':20}))


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog 
        fields = ('title', 'description', 'content', 'image',) # требуется заполнить только поле text
        labels = {'text': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка" } # метка к полю формы text

