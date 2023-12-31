# Generated by Django 4.2 on 2023-04-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_domain_clubmembership_clubapplication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubapplication',
            old_name='domain',
            new_name='domains',
        ),
        migrations.AlterField(
            model_name='clubapplication',
            name='portfolio_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
