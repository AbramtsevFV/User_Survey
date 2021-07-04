# Generated by Django 2.2.10 on 2021-07-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20210702_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('TEXT', 'TEXT'), ('CHOICE', 'CHOICE'), ('MULTICHOICE', 'MULTICHOICE')], default='TEXT', max_length=50, verbose_name='Тип вопроса'),
        ),
    ]
