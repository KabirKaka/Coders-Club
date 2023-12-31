# Generated by Django 4.2 on 2023-04-26 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=25)),
                ('Subtitle', models.CharField(max_length=25)),
                ('author', models.CharField(max_length=25)),
                ('content_summary', models.TextField(max_length=1000)),
                ('slug', models.CharField(max_length=150)),
                ('first_heading', models.CharField(max_length=100)),
                ('second_heading', models.CharField(max_length=100)),
                ('first_paragraph', models.TextField(max_length=1500)),
                ('second_paragraph', models.TextField(max_length=1500)),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='static-images/Blog')),
                ('slider_image1', models.ImageField(blank=True, null=True, upload_to='static-images/Blog')),
                ('slider_image2', models.ImageField(blank=True, null=True, upload_to='static-images/Blog')),
                ('slider_image3', models.ImageField(blank=True, null=True, upload_to='static-images/Blog')),
                ('slider_image4', models.ImageField(blank=True, null=True, upload_to='static-images/Blog')),
                ('slider_image5', models.ImageField(blank=True, null=True, upload_to='static-images/Blog')),
                ('timeStamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
