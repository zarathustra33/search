from django import forms
from django.core import validators
from .import models
from .locations import locations

class CreateArticle(forms.ModelForm):
    class Meta:
        model =models.Article
        fields =['title','body','slug','thumb']


class CreatExperience(forms.ModelForm):
    class Meta:
        model=models.CandidateExperience
        exclude=['canid','expid']

class CreateEdu(forms.ModelForm):
    class Meta:
        model=models.CandidateEdu
        exclude=['canid','eduid']
class UploadResume(forms.ModelForm):
    class Meta:
        # model=models.CandidateInfo
        # fields=[
        # 'name','phone_number','email','work_experience',
        # 'related_work_experience','leadership_experience',
        # 'area_of_focus','linkedin','hunter','bytedance_application_position',
        # 'applied_location','resume_file','location','resume_content'
        # ]
        model=models.CandidateInfo
        exclude=['id']
        

#    phone_number=models.CharField(max_length=264)
#     email=models.EmailField()
#     work_experience=models.IntegerField(null=True)
#     related_work_experience=models.IntegerField(null=True)
#     leadership_experience=models.IntegerField(null=True)
#     area_of_focus=models.CharField(max_length=264)
#     bytedance_application_position=models.CharField(max_length=264)
#     bytedance_application_link=models.URLField(null=True)
#     linkedin=models.URLField(null=True)
#     hunter=models.CharField(max_length=264,null=True)
#     applied_location=models.CharField(max_length=264,null=True)
#     resume_content=models.TextField(default=None)
#     resume_file=models.FileField(default=None,null=True)
#     location=models.CharField(max_length=264,null=True)




    

class SearchCandidate(forms.Form):
    content=forms.CharField(
        required=False,empty_value='',
        widget=forms.TextInput(attrs={'class':"form-control",
        'placeholder':'keywords in Bytedance system or resume',
        'aria-describedby':"sizing-addon1"}),
        label='Profile Keywords',)
    titles=forms.CharField(
        required=False,
        empty_value='',
        widget=forms.TextInput(
            attrs={'class':"form-control",
            'placeholder':'current or past titles'}))
    applied_position =forms.CharField(
        required=False,
        empty_value='',
        widget=forms.TextInput(
            attrs={'class':"form-control",
            'placeholder':'Bytedance position that the candidate is interested in'
            }))
    recent_work=forms.CharField(
        required=False,
        empty_value='',
        widget=forms.TextInput(
            attrs={'class':"form-control",
            'placeholder':'keywords in the last 2 experiences'}))
    companies=forms.CharField(
        required=False,
        empty_value='',
        widget=forms.TextInput(
            attrs={'class':"form-control",
            'placeholder':'current or past companies'}))
    focus=forms.CharField(
        required=False,
        empty_value='',
        widget=forms.TextInput(
            attrs={'class':"form-control",
            'placeholder':'area of focus in the Bytedance hunter system'}))
    location=forms.CharField(
        required=False,
        empty_value='',
        widget=forms.TextInput(
            attrs={'class':"form-control",
            'placeholder':'Bytedance position location or Candidate Profile location, browse available location on the right'}))
    browse_Available_Location=forms.ChoiceField(
        required=False,
        choices=locations,
        widget=forms.Select(attrs={
            'class':"form-control"
        }))
    # work_length=forms.NumberInput(attrs={type:"range"})
    candidate_name=forms.CharField(
        required=False,
        empty_value='',
        widget=forms.TextInput(
            attrs={'class':"form-control",
            'placeholder':'candidate name',
            'aria-describedby':"sizing-addon1"}))
    min_work_length=forms.IntegerField(
        required=False,min_value=0,initial=0,
        widget=forms.NumberInput(attrs={
            'class':"form-control form-control-sm"
        }))
    max_work_length=forms.IntegerField(required=False,min_value=1,initial=35,
    widget=forms.NumberInput(attrs={
            'class':"form-control form-control-sm"
        }))
    
    min_leadership_length=forms.IntegerField(required=False,min_value=0,initial=0,
    widget=forms.NumberInput(attrs={
            'class':"form-control form-control-sm"
        }))
    max_leadership_length=forms.IntegerField(required=False,min_value=1,
    initial=35,
    widget=forms.NumberInput(attrs={
            'class':"form-control form-control-sm"
        }))
    
    botcatcher=forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher) >0:
    #         raisw forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
