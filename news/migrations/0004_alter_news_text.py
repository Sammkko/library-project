# Generated by Django 3.2 on 2022-12-22 04:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
    ]