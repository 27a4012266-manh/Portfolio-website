from django.shortcuts import render, redirect
from .models import Profile, Skill, Project, Blog, ContactInfo, ContactMessage, SocialMedia

def home(request):
    profile = Profile.objects.first()
    social_links = SocialMedia.objects.all()
    context = {
        'profile': profile,
        'social_links': social_links
    }
    return render(request, 'home.html', context)

def about(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'about.html', context)

def skills(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'skills.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)

def blog(request):
    blogs = Blog.objects.all().order_by('-id')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)

def contact(request):
    contact_info = ContactInfo.objects.first()
    social_links = SocialMedia.objects.all()
    
    if request.method == "POST":
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            message=message
        )
        return redirect('contact')
        
    context = {
        'contact_info': contact_info,
        'social_links': social_links
    }
    return render(request, 'contact.html', context)