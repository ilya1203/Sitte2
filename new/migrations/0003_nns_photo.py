# Generated by Django 3.0.2 on 2020-03-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_auto_20200309_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='nns',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]