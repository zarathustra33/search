from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CandidateInfo(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=264)
    phone_number=models.CharField(max_length=264)
    email=models.EmailField()
    work_experience=models.IntegerField(blank=True)
    related_work_experience=models.IntegerField(blank=True)
    leadership_experience=models.IntegerField(blank=True)
    area_of_focus=models.CharField(max_length=264,blank=True)
    bytedance_application_position=models.CharField(max_length=264,blank=True)
    bytedance_application_link=models.URLField(blank=True)
    linkedin=models.URLField(blank=True)
    hunter=models.CharField(max_length=264,blank=True)
    applied_location=models.CharField(max_length=264,blank=True)
    resume_content=models.TextField(default=None,blank=True)
    resume_file=models.FileField(default=None,blank=True)
    location=models.CharField(max_length=264,blank=True)
    def __str__(self):
        return self.name

class CandidateEdu(models.Model):
    canid=models.ForeignKey(CandidateInfo,on_delete=models.CASCADE)
    eduid=models.IntegerField()
    university=models.CharField(max_length=264,blank=True)
    degree=models.CharField(max_length=264,blank=True)
    major=models.CharField(max_length=264,blank=True)
    end_date=models.CharField(max_length=264,blank=True)
    start_date=models.CharField(max_length=264,blank=True)
    def __str__(self):
        return (str(self.canid.id)+' '+self.canid.name+' '+str(self.eduid))

class CandidateExperience(models.Model):
    canid=models.ForeignKey(CandidateInfo,on_delete=models.CASCADE)
    expid=models.IntegerField()
    start_date=models.CharField(max_length=264,blank=True)
    end_date=models.CharField(max_length=264,blank=True)
    company=models.CharField(max_length=264,blank=True)
    position=models.CharField(max_length=264,blank=True)
    job_description=models.TextField(blank=True)
    def __str__(self):
        return (str(self.canid.id)+' '+self.canid.name+' '+str(self.expid))

class Article(models.Model):
    title =models.CharField(max_length=100)
    slug = models.SlugField()
    body =models.TextField()
    # resume = models.FileField()
    date =models.DateTimeField(auto_now_add= True)
    thumb=models.ImageField(default= 'default.png',blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    # add in author later

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+'...'
# class Profile(models.Model):
