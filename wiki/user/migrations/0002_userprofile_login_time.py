# Generated by Django 2.2.6 on 2019-11-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='login_time',
            field=models.DateTimeField(null=True, verbose_name='登录时间'),
        ),
    ]
