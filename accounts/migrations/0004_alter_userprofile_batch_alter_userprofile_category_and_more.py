# Generated by Django 4.2 on 2023-04-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_employment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='batch',
            field=models.CharField(choices=[('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('Older', 'Older')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='category',
            field=models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(choices=[('Karachi', 'Karachi'), ('Hyderabad', 'Hyderabad'), ('Jamshoro', 'Jamshoro')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(choices=[('BCIT', 'BCIT'), ('SE', 'SE'), ('CIS', 'CIS')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='university',
            field=models.CharField(choices=[('NED University', 'NED University'), ('Mehran University', 'Mehran University'), ('Karachi University', 'Karachi University')], max_length=100),
        ),
    ]
