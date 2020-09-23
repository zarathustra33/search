from django.contrib import admin
from .models import Article,CandidateInfo,CandidateEdu,CandidateExperience,RequestLog,ClientCompany,Positions

admin.site.register(Article)
admin.site.register(CandidateInfo)
admin.site.register(CandidateEdu)
admin.site.register(CandidateExperience)
admin.site.register(RequestLog)
admin.site.register(ClientCompany)
admin.site.register(Positions)
# Register your models here.
