# Generated by Django 3.1.3 on 2020-12-10 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='text',
            field=models.TextField(default='Show an example'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travel',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]