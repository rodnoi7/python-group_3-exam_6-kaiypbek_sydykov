from django.db import models

# Create your models here.

class Record(models.Model):
    STAT_ACTIV = 'Active'
    STAT_DEACTIV = 'Blocked'

    STATUS_CHOICES = (
        (STAT_ACTIV, 'Active'),
        (STAT_DEACTIV, 'Blocked')
    )

    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='Автор')
    author_email = models.CharField(max_length=200, null=False, blank=False, verbose_name='Email автора')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус', default='Active')
