from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Validate user data
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not email or not username or not password:
            # Return an error message to the user
            return render(request, 'accounts/register.html', {'error': 'Please fill in all fields'})

        # Create user object
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password     
        )

        # Validate user profile data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        category = request.POST.get('category')
        batch = request.POST.get('batch')
        department = request.POST.get('department')
        university = request.POST.get('university')
        employment_status = request.POST.get('employment_status')
        contact_number = request.POST.get('contact_number')
        facebook_url = request.POST.get('facebook_url')
        github_url = request.POST.get('github_url')
        linkedin_url = request.POST.get('linkedin_url')
        profile_picture = request.FILES.get('profile_picture')
        if not name or not gender or not city or not category or not batch or not department or not university or not employment_status or not contact_number:
            # Delete user object and return an error message to the user
            user.delete()
            return render(request, 'accounts/register1.html', {'error': 'Please fill in all fields'})

        # Create user profile object
        user_profile = UserProfile.objects.create(
            user=user,
            name=name,
            gender=gender,
            city=city,
            category=category,
            batch=batch,
            department=department,
            university=university,
            employment_status=employment_status,
            contact_number=contact_number,
            facebook_url=facebook_url,
            github_url=github_url,
            linkedin_url=linkedin_url,
            profile_picture=profile_picture
        )

        return render(request, 'home/home.html')

    # If this is a GET request (i.e. the user is trying to access the form)
    return render(request, 'accounts/register1.html')

def profile(request):
    return render(request, "accounts/profile.html")

def login(request):
    return render(request, "accounts/login.html")

def joinCommunity(request):
    return render(request, "accounts/joincommunity.html")