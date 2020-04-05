from django.db import models


class  Nns(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
  #  img = models.ImageField(verbose_name='image', upload_to = 'image/')
    
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
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
