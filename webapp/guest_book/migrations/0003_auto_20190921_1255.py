# Generated by Django 2.2.4 on 2019-09-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0002_remove_article_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('author_email', models.CharField(max_length=200, verbose_name='Email автора')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст статьи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Blocked', 'Blocked')], default='Active', max_length=50, verbose_name='Статус')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]