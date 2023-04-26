from django.db import models
from django.contrib.auth.models import User #импортируем модель пользователя

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

"""
Некоторые параметры полей:
on_delete - тип удаления поля
max-length - максимальная длина поля
null = True -  пустые значения будут хранится как NULL в базе данных для полей, где это уместно
unique = True - поле должно быть уникальным
blank = True - поле может быть пустым
default - значение по умолчанию
auto_now=True - для установки поля на текущую дату каждый раз, когда модель сохраняется
"""

class Chat(models.Model): # модель чата
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # поле 'автор чата', связанное с моделью пользоваетеля первичным ключом
    name = models.CharField(max_length=20, unique=True) # строковое поле 'имя чата'
    text = models.TextField(null=True, blank=True, max_length=20) # текстовое поле 'краткое описание чата'
    date = models.DateTimeField(auto_now=True) # поле 'дата создания чата'
    fix = models.BooleanField(default=0) # булевое поле, указывающее на тип закрепления чата (чаты со значением 1 закреплены в списке пользователем, чаты со значением 0 не закреплены)

    class Meta:
        ordering = ['-date'] #сортировка чатов по дате

    def fixed(self):
        """
        метод для закрепления чата
        """
        if self.fix == 0:
            self.fix = 1
        else:
            self.fix = 0

class Message(models.Model): # модель сообщения
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # поле 'пользователь', связанное с моделью пользоваетеля первичным ключом
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True) # поле 'чат', связанное с моделью чата первичным ключом
    words = models.TextField(null=True) # текстовое поле 'содержание сообщения'
    date = models.DateTimeField(auto_now=True) # поле 'дата отправки сообщения'

    class Meta:
        ordering = ['-date']  #сортировка чатов по дате

    def user_name(self):
        return self.user

class Post(models.Model): # модель поста
    author_post = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # поле 'автор поста', связанное с моделью пользоваетеля первичным ключом
    title = models.CharField(max_length=255, unique=True) # строковое поле 'название поста'
    date = models.DateTimeField(auto_now=True, blank=True, null=True) # поле 'дата создания поста'
    content = models.TextField(max_length=10000) # поле 'содержание поста'
    file = models.FileField(upload_to="image-user/%Y/%m/%d/", blank=True, null=True) # загружаемый пользователем файл (в нашем случае картинка)
    filename = models.CharField(blank=True, null=True, max_length=1000) # строковое поле с именем файла
    url_file = models.CharField(blank=True, null=True, max_length=1000) # строковое поле с путём файла

    def file_url(self):
        """
        функция для определения пути файла
        """
        if self.file and hasattr(self.file, 'url'):
            return self.file.url

    class Meta:
        ordering = ['-date'] #сортировка чатов по дате

class Comment(models.Model): # модель комментария
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # поле 'автор комментария', связанное с моделью пользоваетеля первичным ключом
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True) # поле 'пост', связанное с моделью поста первичным ключом
    words = models.TextField(null=True) # текстовое поле с содержанием комментария
    date = models.DateTimeField(auto_now=True) # поле 'дата отправки комментария'

    class Meta:
        ordering = ['-date']


