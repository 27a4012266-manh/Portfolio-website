from django.db import models

# Create your models here.
class Profile(models.Model):
    fullname = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.TextField()
    cv_file = models.FileField(upload_to='cv/')
  def __str__(self):
    return self.fullname

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_category = models.CharField(max_length=100)
    achievement = models.TextField()
  def __str__(self):
    return self.skill_name

class Project(models.Model):
    Project_title = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    short_description = models.TextField()
    github_link = models.URLField()
  def __str__(self):
    return self.Project_title

class Blog(models.Model):
    Blog_title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.Blog_title

class Contact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=300)
  def __str__(self):
    return "Contact Information"
    
class SocialMedia(models.Model):
    icon = models.ImageField(upload_to='social_icon/')
    socialmedia_title = models.CharField(max_length=200)
    link = models.URLField()
  def __str__(self):
    return self.socialmedia_title
