# Generated by Django 2.0.6 on 2018-07-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_management', '0003_auto_20180727_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='troublerecord',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='备注'),
        ),
    ]