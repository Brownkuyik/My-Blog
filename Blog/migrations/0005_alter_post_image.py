# Generated by Django 3.2.15 on 2022-10-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='featured_image/'),
        ),
    ]
