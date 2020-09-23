from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article,CandidateInfo,CandidateEdu,CandidateExperience,RequestLog
from django.contrib.auth.decorators import login_required
from .import forms
import datetime
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# from haystack.query import SearchQuerySet
# from whoosh.qparser import QueryParser,MultifieldParser
from whoosh import query
import whoosh.index as index
from .locations import locations
import pickle
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
## import my functions to generate email htmls
from .send_email import group_candidates,hunterEmails,generate_body_html
import os
# parent_dir=os.path.abspath(os.getcwd())
parent_dir=os.getcwd()
# ix = index.open_dir("/Users/xujiahui/Downloads/ocbang/bytedance database/recent experience index")
ix = index.open_dir(parent_dir+'/articles/recent experience index')
def load_obj(name ):
    with open(parent_dir+'/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

structured_profiles=load_obj('bytedance_dictionary_with_loc_renamed')
from .whoosh_search import content_search, applied_position_search,location_search,recent_experience_search,company_search,title_search,initiate


# Create your views here.
def article_list(request):
    articles=Article.objects.all().order_by('date')## 把这个发送给view

    paginator=Paginator(articles,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page('page')


    return render(request,'articles/article_list.html',{'listings':paged_listings})## send the data to the template

def article_detail(request,slug):
    # return HttpResponse(slug)
    article=Article.objects.get(slug=slug)
    return render(request,'article_detail.html',{"article":article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method=='POST':
        
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            # save article to bd
            instance = form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list') 
    else:

        form = forms.CreateArticle()
        return render(request,'articles/article_create.html',{'form':form})


@login_required(login_url="/accounts/login/")
def upload_resume(request):
    if request.method=='POST':
        
        formResume=forms.UploadResume(request.POST,request.FILES)
        formExp=forms.CreatExperience(request.POST)
        formEdu=forms.CreateEdu(request.POST)
        if formResume.is_valid():
            # save article to bd
            instance = formResume.save(commit=False)
            if instance.hunter=='':
                instance.hunter=request.user
            instance.save()
        if formExp.is_valid():
            expinstance=formExp.save(commit=False)
            print(expinstance)
            print(CandidateInfo.id)
            expinstance.canid=CandidateInfo.objects.get(id=CandidateInfo.id)
            expinstance.save()



            return redirect('articles:search') 
    else:

        formResume = forms.UploadResume()
        formExp=forms.CreatExperience()
        formEdu=forms.CreateEdu()
        return render(request,'articles/upload_resume.html',{'formResume':formResume,'formExp':formExp,'formEdu':formEdu})

# def search(request):
#     listings=Article.objects.all()
#         # keywords
#     if 'keywords' in request.GET:
#         keywords=request.GET['keywords']
#         queryset_list=queryset_list.filter(description__icontains=keywords)
@login_required(login_url="/accounts/login/")
def search_view(request):
    form = forms.SearchCandidate()
    if request.method=='POST':
        print(request.POST.dict())
        if request.POST.get('email_title')!=None:
            print('roger that ')
            checked=request.POST.getlist('checks')
            position=request.POST.get('email_title')
            print(checked)
            
            logged_in_user=request.user.first_name
            checked_ids=[int(ident) for ident in checked]

            filtered_result=[p for p in structured_profiles if p['id'] in checked_ids]
            luckyRecruiter=list(set([p['hunter'] for p in filtered_result]))
            print(luckyRecruiter)

            matched_candidates=group_candidates(luckyRecruiter,filtered_result,hunterEmails)
            print(len(matched_candidates))

            hunters=matched_candidates.keys()
            subject = 'OCBang Alert: you have candidates matched with ' + position
            for lucky_hunter in hunters:
                grouped_candidates=matched_candidates[lucky_hunter]
                RECIPIENT=hunterEmails[lucky_hunter]
                BODY_HTML=generate_body_html(grouped_candidates,position,lucky_hunter)
                # from_email='sharon.xu@ocbang.com'
                from_email=hunterEmails[logged_in_user]
                text_content='you have matched up candidates alert!'
            # ## send emails 
            # subject, from_email, to = 'hello', 'sharon.xu@ocbang.com', 'sharon.xu@ocbang.com'
            
            # html_content = '<p>This is an <strong>important</strong> message.</p>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [RECIPIENT])
                msg.attach_alternative(BODY_HTML, "text/html")
                msg.send()  
            
            return render(request,'articles/email_success.html',{'hunters':hunters})
        else:
    # if request.method=='POST':
        #form=forms.SearchCandidate(request.POST)
            # articles=SearchQuerySet().autocomplete(content_auto=request.POST.get('titles',''))
            
            ## save the search record to the database


            logged_in_user=request.user.first_name
            
            titles_kw=request.POST.get('titles','')
            applied_position_kw=request.POST.get('applied_position','')
            content_kw=request.POST.get('content','') 
            recent_kw=request.POST.get('recentWork','') 
            company_kw=request.POST.get('companies','') 
            location_kw=request.POST.get('location','')
            name_kw=request.POST.get('candidate_name','')
            work_lower_limit=request.POST.get('min_work_length',0)
            work_upper_limit=request.POST.get('max_work_length',50)
            leadership_lower_limit=request.POST.get('min_leadership_length',default=0)
            leadership_upper_limit=request.POST.get('max_leadership_length')
           ### save the request.
            search_request,status=RequestLog.objects.get_or_create(
                content_requst=content_kw,
                applied_positon_request=applied_position_kw,
                recent_work_request=recent_kw,
                companies_request=company_kw,
                titles_request=titles_kw,
                location_request=location_kw,
                min_work_length_request=work_lower_limit,
                max_work_length_request=work_upper_limit,
                min_leadership_length_request=leadership_lower_limit,
                max_leadership_length_request=leadership_upper_limit,
                user=request.user,
                time=datetime.datetime.now()
            )
            print(search_request)
            print(status)
            print('request saved')
           
           
           
            if leadership_lower_limit=='':
                leadership_lower_limit=0
            if leadership_upper_limit=='':
                leadership_upper_limit=50

            if content_kw=='' and applied_position_kw=='' and titles_kw=='' and recent_kw=='' and company_kw=='' and location_kw=='':

                return render(request,'articles/enter_keywords.html')

            content_res=initiate
            applied_position_res=initiate
            recent_res=initiate
            company_res=initiate
            title_res=initiate
            location_res=initiate

            if content_kw!='':
                content_res=content_search(content_kw)
            
            if applied_position_kw!='':
                applied_position_res=applied_position_search(applied_position_kw)
            
            if titles_kw!='':
                title_res=title_search(titles_kw)
            if recent_kw!='':

                recent_res=recent_experience_search(recent_kw)
            if company_kw!='':
                company_res=company_search(company_kw)
            if location_kw!='':
                location_res=location_search(location_kw)

            final_result=list(set(content_res).intersection(set(applied_position_res)).intersection(set(recent_res)).intersection(set(company_res)).intersection(set(title_res)).intersection(set(location_res)))
            
            result_profiles=CandidateInfo.objects.filter(id__in=final_result)
            result_profiles=result_profiles.filter(work_experience__gte=int(work_lower_limit))
            result_profiles=result_profiles.filter(work_experience__lte=int(work_upper_limit))
            result_profiles=result_profiles.filter(leadership_experience__gte=int(leadership_lower_limit))
            result_profiles=result_profiles.filter(leadership_experience__lte=int(leadership_upper_limit))
            '''
            result_profiles=[p for p in structured_profiles if p['id'] in final_result]
            result_profiles=[p for p in result_profiles if p['work_experience']>=int(work_lower_limit) and p['work_experience']<=int(work_upper_limit)]
            result_profiles=[p for p in result_profiles if p['leadership_experience']>=int(leadership_lower_limit) and p['leadership_experience']<=int(leadership_upper_limit)]
            
            
            if name_kw!='':
                result_profiles=[p for p in result_profiles if name_kw.lower() in p['name'].lower()]
            '''
            result_profile_ids=[p.id for p in result_profiles]
            result_exps=CandidateExperience.objects.filter(canid_id__in=result_profile_ids)

            if str(logged_in_user) not in ['sharon','audrey','nina','lewis','kirby','ella']:
            #     print(logged_in_user)
            #     print('is not in the account manager list')
                result_profiles=result_profiles.filter(hunter=str(logged_in_user))
                result_profile_ids=[p.id for p in result_profiles]
                result_exps=CandidateExperience.objects.filter(canid_id__in=result_profile_ids)
                # result_profiles=[p for p in result_profiles if p.get('hunter')==str(logged_in_user)]


            # return render(request,'articles/search.html',{'form':form,'articles':articles})
            # return redirect('articles/article_list.html')
            
            return render(request,'articles/search_result.html',{'profiles':result_profiles,'exps':result_exps})
            # return render(request,'articles/search.html',{'profiles':result_profiles,'form':form,'locChoice':locations})

    else:
    
        return render(request,'articles/search.html',{'form':form,'locChoice':locations})

