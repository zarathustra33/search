from django import forms
from django.core import validators
from .import models
from .locations import locations

class CreateArticle(forms.ModelForm):
    class Meta:
        model =models.Article
        fields =['title','body','slug']
        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'body':forms.Textarea(attrs={
                'class':'form-control'
            }),
            'slug':forms.TextInput(attrs={
                'class':'form-control'
            }),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['body'].label='Your Announcement Here'


class CreatExperience(forms.ModelForm):
    class Meta:
        model=models.CandidateExperience
        exclude=['canid','expid']
        widgets = {
            'company': forms.TextInput(attrs={
            'class':"form-control"
        }),
        'position': forms.TextInput(attrs={
            'class':"form-control"
        }),
        'job_description': forms.Textarea(attrs={
            'class':"form-control"
        }),
        'start_date':forms.DateInput(attrs={
                'type': 'date',
                'class':"form-control"}),
        'end_date':forms.DateInput(attrs={
                'type': 'date',
                'class':"form-control"}),
        }
        # fields='__all__'


class SurveyForm(forms.ModelForm):
    class Meta:
        model=models.OrgDept
        fields=['name','parent']
        widgets={
            'name':forms.Select(attrs={
            'class':'form-control'}
        )

        }


class CreateEdu(forms.ModelForm):
    degree=forms.ChoiceField(choices=[
        ('associate','Associate'),
        ('bachelor','Bachelor'),
        ('master','Master'),
        ('doctor','Doctor')],
        widget=forms.Select(attrs={
            'class':"form-control"
        }))
    class Meta:
        model=models.CandidateEdu
        exclude=['canid','eduid']
        widgets = {
            'university': forms.TextInput(attrs={
            'class':"form-control"
        }),
        'degree':forms.Select(
        attrs={
            'class':"form-control"
        }),
        'major': forms.TextInput(attrs={
            'class':"form-control"
        }),
        }
        # fields='__all__'
'''
class CandidateStatusform(forms.ModelForm):
    class Meta:
        model=models.CandidateStatus
        exclude=['candidate','id']
'''

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
        exclude=['id','create_date']
        widgets = {
            'applied_company': forms.Select(attrs={
            'class':"form-control"
        }),
            'area_of_focus': forms.TextInput(attrs={
            'class':"form-control"
        }),
            'client_position':forms.Select(attrs={
            'class':"form-control"
        }),
            'status':forms.TextInput(attrs={
            'class':"form-control"
        }),
            # 'resume_submited_date':forms.TextInput(attrs={
            # 'class':"form-control"}),
            'name':forms.TextInput(attrs={
            'class':"form-control"
        }),
             'phone_number':forms.TextInput(attrs={
            'class':"form-control"}),
            'email':forms.EmailInput(attrs={
            'class':"form-control"
        }),
            'location':forms.TextInput(attrs={
            'class':"form-control"}),
            'flag_experience':forms.CheckboxInput(attrs={
            'class':"form-control-sm"}),
            'linkedin':forms.URLInput(attrs={
            'class':"form-control"}),
            'resume_submited_date':forms.DateInput(attrs={
                'type': 'date',
                'class':"form-control"}),
            'resume_file':forms.FileInput(attrs={
               
                'class':"form-control-file"}),
            
            'work_experience':forms.NumberInput(attrs={
            'class':"form-control form-control-sm",'min':0
        }),
            'related_work_experience':forms.NumberInput(attrs={
            'class':"form-control form-control-sm",'min':0
        }),
            'leadership_experience':forms.NumberInput(attrs={
            'class':"form-control form-control-sm",'min':0
        })
        }

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


class OrgSurveyForm(forms.ModelForm):
    class Meta:
        model=models.OrgSurvey
        fields='__all__'
        widgets={
            'company': forms.Select(attrs={
            'class':"form-control"}),
            'department': forms.Select(attrs={
            'class':"form-control"}),
            'team': forms.TextInput(attrs={
            'class':"form-control"}),
            'other_department': forms.TextInput(attrs={
            'class':"form-control"}),
            'self_provide_dept':forms.TextInput(attrs={
            'class':"form-control"}),
            'team_size':forms.NumberInput(attrs={
            'class':"form-control"}),
            'base_expectation':forms.NumberInput(attrs={
            'class':"form-control"}),
            'total_expectation':forms.NumberInput(attrs={
            'class':"form-control"}),
            'will_to_china':forms.Select(attrs={
            'class':"form-control"}),
            'team_management':forms.Select(attrs={
            'class':"form-control"}),
            'people_in_lead':forms.NumberInput(attrs={
            'class':"form-control"}),
            'reason_for_departure':forms.Select(attrs={
            'class':"form-control"}),
            'other_reason_for_departure':forms.TextInput(attrs={
            'class':"form-control"})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = models.OrgDept.objects.none()

        if 'company' in self.data:
            try:
                # company_id=int(self.data.get('company'))
                company_id=int(self.data.get('company'))
                self.fields['department'].queryset=models.OrgDept.objects.filter(parent_id=company_id).order_by('name')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['department'].queryset=self.instance.company.department_set.order_by('name')