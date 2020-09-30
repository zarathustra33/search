from django.contrib import admin
from .models import Article,CandidateInfo,CandidateEdu,CandidateExperience,RequestLog,OrgCompany,OrgDept
# ,ClientCompany,Positions

admin.site.register(Article)
admin.site.register(CandidateInfo)
admin.site.register(CandidateEdu)
admin.site.register(CandidateExperience)
admin.site.register(RequestLog)
admin.site.register(OrgCompany)
admin.site.register(OrgDept)
# admin.site.register(CandidateStatus)
# admin.site.register(ClientCompany)
# admin.site.register(Positions)
# Register your models here.
