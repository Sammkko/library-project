# Generated by Django 3.2 on 2023-01-08 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20230102_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='history_image',
            new_name='c_image',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинки'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
