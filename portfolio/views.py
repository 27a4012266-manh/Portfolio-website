from django.shortcuts import render
from .models import *

def home(request):
    profile = Profile.objects.first()
    socials = SocialMedia.objects.all()
    context = {
        'profile': profile,
        'socials': socials
    }
    return render(
        request,
        'home.html',
        context
    )

def about(request):

    profile = Profile.objects.first()

    contact_info = ContactInfo.objects.first()

    context = {
        'profile': profile,
        'contact_info': contact_info
    }

    return render(
        request,
        'about.html',
        context
    )

def skills(request):
    profile = Profile.objects.first()

    technical_skills = Skill.objects.filter(
        skill_category='Technical'
    )

    other_skills = Skill.objects.filter(
        skill_category='Other'
    )

    return render(
        request,
        'skills.html',
        {
            'profile': profile,
            'technical_skills': technical_skills,
            'other_skills': other_skills,
        }
    )

def projects(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()

    return render(request, 'projects.html', {
        'profile': profile,
        'projects': projects
    })

def blog(request):
    profile = Profile.objects.first()
    blogs = Blog.objects.all()
    context = {
        'profile': profile,
        'blogs': blogs
    }
    return render(request, 'blog.html', context)

from .models import *

def contact(request):

    profile = Profile.objects.first()
    contact_info = ContactInfo.objects.first()
    socials = SocialMedia.objects.all()

    if request.method == "POST":

        ContactMessage.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )

    context = {
        'profile': profile,
        'contact_info': contact_info,
        'socials': socials,
    }

    return render(request, 'contact.html', context)