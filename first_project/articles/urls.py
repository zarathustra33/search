from django.conf.urls import url
from django.urls import path
from .import views

app_name='articles'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^$',views.index,name='index'),
    # url(r'^about/$',views.about),
    url(r'^$',views.article_list,name='list'),
    url(r'^create/$',views.article_create,name='create'),
    url(r'^search/$',views.search_view,name='search'),
    url(r'^upload/$',views.upload_resume,name='upload'),
    url(r'^board/',views.PersonalBoard.as_view(),name='board'),
    path('candidate/<int:pk>',views.CandidateDetailView.as_view(),name='detail'),
    path('survey/<int:pk>',views.OrgSurvey,name='survey'),
    path('update/<int:pk>',views.CandidateUpdateView.as_view(),name='candidate-update'),
    path('ajax/load-depts/',views.load_depts,name='ajax_load_depts'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail,name="detail"),
    
]
