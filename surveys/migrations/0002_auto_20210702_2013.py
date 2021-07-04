# Generated by Django 2.2.10 on 2021-07-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='survey',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.AlterModelOptions(
            name='variants',
            options={'verbose_name': 'Вариант', 'verbose_name_plural': 'Варианты'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(default=123, max_length=150, verbose_name='Вопрос'),
            preserve_default=False,
        ),
    ]
