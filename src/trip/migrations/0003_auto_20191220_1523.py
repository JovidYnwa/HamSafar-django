# Generated by Django 2.2.7 on 2019-12-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=250, verbose_name='Оставьте комментарий'),
        ),
    ]
