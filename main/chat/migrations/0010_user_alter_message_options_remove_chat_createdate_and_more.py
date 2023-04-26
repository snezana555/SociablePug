# Generated by Django 4.1.5 on 2023-01-10 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_alter_chat_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('password', models.IntegerField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='chat',
            name='createdate',
        ),
        migrations.RemoveField(
            model_name='message',
            name='createdate',
        ),
        migrations.AlterField(
            model_name='chat',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.user'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.user'),
        ),
    ]
