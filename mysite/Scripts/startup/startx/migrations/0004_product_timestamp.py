# Generated by Django 2.1.4 on 2018-12-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startx', '0003_auto_20181227_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]