from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CandidateInfo(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=264)
    phone_number=models.CharField(max_length=264)
    email=models.EmailField()
    work_experience=models.IntegerField(blank=True,null=True)
    related_work_experience=models.IntegerField(blank=True,null=True)
    leadership_experience=models.IntegerField(blank=True,null=True)
    area_of_focus=models.CharField(max_length=264,blank=True,null=True)
    bytedance_application_position=models.CharField(max_length=264,blank=True,null=True)
    bytedance_application_link=models.URLField(blank=True,null=True)
    linkedin=models.URLField(blank=True,null=True)
    hunter=models.CharField(max_length=264,blank=True,null=True)
    applied_location=models.CharField(max_length=264,blank=True,null=True)
    resume_content=models.TextField(default=None,blank=True,null=True)
    resume_file=models.FileField(default=None,blank=True,null=True)
    location=models.CharField(max_length=264,blank=True,null=True)
    def __str__(self):
        return self.name

class CandidateEdu(models.Model):
    canid=models.ForeignKey(CandidateInfo,on_delete=models.CASCADE)
    eduid=models.IntegerField()
    university=models.CharField(max_length=264,blank=True,null=True)
    degree=models.CharField(max_length=264,blank=True,null=True)
    major=models.CharField(max_length=264,blank=True,null=True)
    end_date=models.CharField(max_length=264,blank=True,null=True)
    start_date=models.CharField(max_length=264,blank=True,null=True)
    def __str__(self):
        return (str(self.canid.id)+' '+self.canid.name+' '+str(self.eduid))

class CandidateExperience(models.Model):
    canid=models.ForeignKey(CandidateInfo,on_delete=models.CASCADE)
    expid=models.IntegerField()
    start_date=models.CharField(max_length=264,blank=True,null=True)
    end_date=models.CharField(max_length=264,blank=True,null=True)
    company=models.CharField(max_length=264,blank=True,null=True)
    position=models.CharField(max_length=264,blank=True,null=True)
    job_description=models.TextField(blank=True,null=True)
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


class RequestLog(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content_requst=models.CharField(null=True,max_length=512)
    applied_positon_request=models.CharField(null=True,max_length=512)
    recent_work_request=models.CharField(null=True,max_length=512)
    titles_request=models.CharField(null=True,max_length=512)
    companies_request=models.CharField(null=True,max_length=264)
    location_request=models.CharField(null=True,max_length=264)
    min_work_length_request=models.IntegerField(null=True)
    max_work_length_request=models.IntegerField(null=True)
    min_leadership_length_request=models.IntegerField(null=True)
    max_leadership_length_request=models.IntegerField(null=True)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (str(self.user.first_name)+' '+str(self.time))

class ClientCompany(models.Model):
    name=models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Positions(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    company=models.ForeignKey(ClientCompany,on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    location=models.CharField(max_length=64,null=True)
    account_manager=models.CharField(max_length=128,null=True)
    tips=models.TextField(default=None,blank=True,null=True)
    description=models.TextField(default=None,blank=True,null=True)
    file=models.FileField(blank=True)
    def __str__(self):
        return(str(self.id)+' '+self.company.name+' '+self.name)      