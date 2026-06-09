from django.shortcuts import render
from .models import *


from django.shortcuts import render
from .models import Profile, SocialMedia

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

    context = {
        'profile': profile,
        'technical_skills': technical_skills,
        'other_skills': other_skills,
    }

    return render(request, 'skills.html', context)


def projects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'projects.html', context)


def blogs(request):
    blogs = Blog.objects.all().order_by('-publish_date')

    context = {
        'blogs': blogs
    }

    return render(request, 'blogs.html', context)


def contact(request):
    contact_info = Contact.objects.first()
    social_media = SocialMedia.objects.all()

    context = {
        'contact': contact_info,
        'social_media': social_media
    }

    return render(request, 'contact.html', context)


