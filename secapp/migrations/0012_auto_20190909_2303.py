# Generated by Django 2.2.4 on 2019-09-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secapp', '0011_auto_20190909_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dost',
            name='dost_link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='offer_link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
