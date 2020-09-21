import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()

import pickle

def load_obj(name ):
    with open('/Users/xujiahui/Downloads/ocbang/data/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

structured_profiles=load_obj('bytedance_dictionary_with_loc_renamed')

from articles.models import CandidateInfo,CandidateEdu,CandidateExperience

def populate_edu():

    for p in structured_profiles:
        canid=p['id']
        education=p['education']
        for i in range(len(education)):
            info_obj=CandidateInfo.objects.get(id=canid)
            eduid=i
            university=education[i]['University']
            degree=education[i].get('Education background','')
            major=education[i].get('Major','')
            start_date=education[i]['Graduation date'].split('~')[0]
            end_date=education[i]['Graduation date'].split('~')[1]
            A_edu=CandidateEdu.objects.get_or_create(
                canid=info_obj,
                eduid=eduid,
                university=university,
                degree=degree,
                major=major,
                start_date=start_date,
                end_date=end_date
            )[0]

def populate_experience():
    for p in structured_profiles:
        canid=p['id']
        experience=p['experience']
        experience_length=len(experience)
        for i in range(experience_length):
            info_obj=CandidateInfo.objects.get(id=canid)
            expid=i
            start_date=experience[i]['Time'].split('~')[0]
            end_date=experience[i]['Time'].split('~')[1]
            company=experience[i]['Company']
            position=experience[i]['Position']
            job_description=experience[i].get('Job description','')

            A_exp=CandidateExperience.objects.get_or_create(
                canid=info_obj,
                expid=expid,
                start_date=start_date,
                end_date=end_date,
                company=company,
                position=position,
                job_description=job_description
            )[0]
 
def populate_info():
    for p in structured_profiles:
        id=p['id']
        name=p['name']
        phone_number=p['phone number']
        email=p['email']
        work_experience=p['work_experience']
        related_work_experience=p['related_work_experience']
        leadership_experience=p['leadership_experience']
        area_of_focus=p['area_of_focus']
        bytedance_application_position=p['bytedance_application_position']
        bytedance_application_link=p['bytedance_application_link']
        linkedin=p['linkedin url']
        hunter=p['hunter']
        applied_location=p.get('applied_location','')
        resume_content=p.get('file content','')
        location=p.get('location','')
        
        A_info=CandidateInfo.objects.get_or_create(
            id=id,
            name=name,
            phone_number=phone_number,
            email=email,
            work_experience=work_experience,
            related_work_experience=related_work_experience,
            leadership_experience=leadership_experience,
            area_of_focus=area_of_focus,
            bytedance_application_position=bytedance_application_position,
            bytedance_application_link=bytedance_application_link,
            linkedin=linkedin,
            hunter=hunter,
            applied_location=applied_location,
            resume_content=resume_content,
            location=location

        )[0]

if __name__=='__main__':
    # populate_info()
    # populate_experience()
    populate_edu()
    print('populating info complete!')
