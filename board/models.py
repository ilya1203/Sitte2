from django.db import models

class Cont(models.Model):
    title = models.CharField(max_length=50)
    textContent = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    class Meta:
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True,
    verbose_name = 'Название')
    def __str__(self):
        return self.name

    class Meta:
            verbose_name_plural = 'Рубрики'
            verbose_name = 'Рубрика'
            ordering = ['name']
