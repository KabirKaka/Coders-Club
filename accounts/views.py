from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.views.generic import DetailView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def save_profile_picture(profile_picture):
    # create an instance of FileSystemStorage class to manage file storage
    fs = FileSystemStorage()

    # create the directory if it does not exist
    directory = os.path.join(settings.MEDIA_ROOT, 'profile_pics')
    if not os.path.exists(directory):
        os.makedirs(directory)

    # save the uploaded file to the directory
    filename = fs.save(os.path.join(directory, profile_picture.name), profile_picture)

    # get the file's url
    profile_pic_url = fs.url(filename)
    if profile_pic_url.startswith('/media/'):
        profile_pic_url = profile_pic_url[len('/media/'):]  
    return profile_pic_url

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
            return render(request, 'accounts/register.html', {'error': 'Please fill in all fields'})

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

        login_django(request, user)
        return redirect('home')

    # If this is a GET request (i.e. the user is trying to access the form)
    if not request.user.is_authenticated:
        return render(request, 'accounts/register.html')
    else:            
        return redirect('account-profile')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('account-login')
    else:                
        return render(request, "accounts/profile.html")

def editprofilepicture(request):
    if not request.user.is_authenticated:
        return redirect('account-login')
    else:                
        if request.method == 'POST':            
            profile_picture = request.FILES.get('profile_picture')
            request.session['profile_picture_link'] = save_profile_picture(profile_picture)
            return redirect('account-editprofile')
        return redirect('account-editprofile')
    
def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('account-login')
    else:                
        user_profile = request.user.profile
        if request.method == 'POST':
            user_profile.name = request.POST.get('name')
            user_profile.employment_status = request.POST.get('employment_status')
            user_profile.category = request.POST.get('category')
            user_profile.city = request.POST.get('city')
            user_profile.contact_number = request.POST.get('contact_number')
            profile_picture = request.session.get('profile_picture_link')
            if profile_picture:
                user_profile.profile_picture = profile_picture            
            user_profile.save()
            return redirect('account-profile')
        return render(request, "accounts/editprofile.html", {"temp_profile_pic": request.session.get('profile_picture_link')})

    
class PublicProfile(DetailView):
    model = UserProfile
    template_name = 'accounts/publicprofile.html'
    # def get_object(self):
    #     username = self.kwargs.get('username')
    #     return User.objects.get(username=username)  

    slug_field = "user__username"

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_django(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid credentials. Please try again.'
            return render(request, 'accounts/login.html', {'error_message': error_message})
    else:
        if not request.user.is_authenticated:
            return render(request, 'accounts/login.html')
        else:            
            return redirect('home')

def logout(request):
    logout_django(request)
    return redirect('account-login')

def joinCommunity(request):
    if not request.user.is_authenticated:
        return redirect('account-login')
    else:            
        return render(request, "accounts/joincommunity.html")
