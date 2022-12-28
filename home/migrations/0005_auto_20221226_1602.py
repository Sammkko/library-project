# Generated by Django 3.2 on 2022-12-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Readers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинки')),
            ],
            options={
                'verbose_name': 'Читателям',
                'verbose_name_plural': 'Читателям',
            },
        ),
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': 'Каталоги', 'verbose_name_plural': 'Каталоги'},
        ),
        migrations.AddField(
            model_name='ads',
            name='ads_date',
            field=models.DateField(auto_now=True),
        ),
    ]
