# Generated by Django 2.0.6 on 2018-07-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_management', '0005_auto_20180728_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployrecord',
            name='deploy_time',
            field=models.DateTimeField(verbose_name='上线时间'),
        ),
    ]