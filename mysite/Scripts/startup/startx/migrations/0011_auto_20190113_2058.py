# Generated by Django 2.1.4 on 2019-01-13 15:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startx', '0010_product_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]
