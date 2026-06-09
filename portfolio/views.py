from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
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
    blog = Blog.objects.all()
    context = {
        'profile': profile,
        'blog': blog
    }
    return render(request, 'blog.html', context)

def contact(request):
    form = ContactMessageForm()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gửi tin nhắn thành công!')
            return redirect('contact')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin.')
    return render(request, 'contact.html', {'form': form})