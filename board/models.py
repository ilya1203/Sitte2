from django.db import models


class Works(models.Model):

    title = models.CharField(max_length=50, verbose_name="Название")
    comment = models.TextField(verbose_name='Описание')
    URL = models.TextField(verbose_name='URL')
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Загруженно')
    
