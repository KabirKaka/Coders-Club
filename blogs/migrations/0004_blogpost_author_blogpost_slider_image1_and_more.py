# Generated by Django 4.2 on 2023-04-27 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_blogpost_author_remove_blogpost_slider_image1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(blank=True, default="Coder's Club", max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slider_image1',
            field=models.ImageField(blank=True, null=True, upload_to='static-images/Blog'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slider_image2',
            field=models.ImageField(blank=True, null=True, upload_to='static-images/Blog'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slider_image3',
            field=models.ImageField(blank=True, null=True, upload_to='static-images/Blog'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slider_image4',
            field=models.ImageField(blank=True, null=True, upload_to='static-images/Blog'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slider_image5',
            field=models.ImageField(blank=True, null=True, upload_to='static-images/Blog'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default=3, max_length=150),
            preserve_default=False,
        ),
    ]
