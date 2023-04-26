from django.apps import AppConfig
"""
 Этот файл создан, чтобы помочь пользователю включить в приложение конфигурацию приложения для приложения.
 Создаётся django при создании приложения с помощью "django-admin startapp <name_project>"
"""
class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
