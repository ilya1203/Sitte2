from django.db import models



class Comments(models.Model):
    Name = models.CharField(max_length=25, verbose_name='Your Name')
    Text = models.TextField(blank=True, verbose_name='Your comment')
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'
        ordering = ['-published']
# Create your models here.
