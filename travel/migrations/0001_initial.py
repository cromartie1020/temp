# Generated by Django 3.1.3 on 2020-12-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
