from django.contrib import admin
from .models import Article,CandidateInfo,CandidateEdu,CandidateExperience

admin.site.register(Article)
admin.site.register(CandidateInfo)
admin.site.register(CandidateEdu)
admin.site.register(CandidateExperience)
# Register your models here.
