from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    EMPLOYMENT_CHOICES = (
        ('Internee', 'Internee'),
        ('Full-time Job', 'Full-time Job'),
        ('Part-time Job', 'Part-time Job'),
        ('Freelancer', 'Freelancer'),
        ('None', 'None'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    CITY_CHOICES = (
        ('Karachi', 'Karachi'),
        ('Hyderabad', 'Hyderabad'),
        ('Jamshoro', 'Jamshoro'),
    )

    CATEGORY_CHOICES = (
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
    )

    BATCH_CHOICES = (
        ('2022', '2022'),
        ('2021', '2021'),
        ('2020', '2020'),
        ('Older', 'Older'),
    )

    DEPARTMENT_CHOICES = (
        ('BCIT', 'BCIT'),
        ('SE', 'SE'),
        ('CIS', 'CIS'),
    )   

    UNIVERSITY_CHOICES = (
        ('NED University', 'NED University'),
        ('Mehran University', 'Mehran University'),
        ('Karachi University', 'Karachi University'),
    )     
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    batch = models.CharField(max_length=20, choices=BATCH_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    university = models.CharField(max_length=100, choices=UNIVERSITY_CHOICES)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)
    contact_number = models.CharField(max_length=20)
    facebook_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    profile_picture = models.ImageField(default='https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg', upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.name