from django.contrib import admin
from .models import Chat, Message, Post, Comment # импортируем модели из файла

admin.site.register(Chat) # регистрируем модель чата
admin.site.register(Message) # регистрируем модель сообщения

admin.site.register(Post) # регистрируем модель поста
admin.site.register(Comment) # регистрируем модель комментария

"""
при входе в панель администратора ('localhost:8000/admin') мы можем управлять регистрируемыми моделями
"""