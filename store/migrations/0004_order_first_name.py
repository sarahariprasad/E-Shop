# Generated by Django 3.1.1 on 2020-09-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200924_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
