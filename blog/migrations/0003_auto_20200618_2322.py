# Generated by Django 3.0.7 on 2020-06-19 04:22

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200618_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]