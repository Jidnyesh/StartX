# Generated by Django 2.1.4 on 2019-01-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startx', '0021_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='required_skills',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='requirements',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
