# Generated by Django 2.1.4 on 2019-01-25 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startx', '0015_advertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='income',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='project_number',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
