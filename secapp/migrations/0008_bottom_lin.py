# Generated by Django 2.2.4 on 2019-09-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secapp', '0007_offers'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottom',
            name='lin',
            field=models.URLField(default=''),
        ),
    ]
