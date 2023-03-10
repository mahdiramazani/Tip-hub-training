# Generated by Django 4.1.4 on 2023-01-03 08:10

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[500, 300], upload_to='media/blog/image'),
        ),
    ]
