# Generated by Django 2.2.4 on 2019-09-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secapp', '0005_dost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_image', models.ImageField(upload_to='Services')),
                ('service_alter', models.CharField(max_length=50)),
                ('service_desc', models.TextField()),
                ('service_link', models.URLField()),
            ],
        ),
    ]
