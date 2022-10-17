from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='images',verbose_name='Картинки')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    news_view = models.IntegerField(default=0)

    class Meta:
        ordering = ('-create_date',)
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.title} - {self.create_date}'