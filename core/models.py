from django.db import models
from django.contrib.auth.models import User
from .middleware import get_current_user
from django.db.models import Q


# Create your models here.
class Articles(models.Model):
    """
    Основная модель для хранения статей (инструкций)

    :param author: ForeignKey к модели :class:`django.contrib.auth.models.User`
    :param name: название статьи
    :param create_date: дата создания статьи, хранится в формате объекта `datetime.datetime()`
    :param text: содержание статьи
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец статьи', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'


class StatusFilterComments(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            Q(status=False, author=get_current_user()) | Q(status=False, article__author=get_current_user()) | Q(
                status=True))


class Comments(models.Model):
    """
    Модель хранения комментариев к статьям

    :param article: ForeignKey к модели `django.contrib.auth.models.Articles`
    :param author: ForeignKey `django.contrib.auth.models.User`
    :param create_date: дата создания комментария, хранится в формате объекта `datetime.datetime()`
    :param text: содержание комментария
    :param status: статус комментрия - одобрен, неодобрен
    """
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True,
                                related_name='comments_articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)
    objects = StatusFilterComments()
