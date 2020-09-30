from django.conf.urls import url
from django.urls import path
from .import views

app_name='positions'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^$',views.index,name='index'),
    # url(r'^about/$',views.about),
    # url(r'^$',views.article_list,name='list'),
    # url(r'^create/$',views.article_create,name='create'),
    # url(r'^search/$',views.search_view,name='search'),
    # url(r'^upload/$',views.upload_resume,name='upload'),
    # url(r'^(?P<slug>[\w-]+)/$',views.article_detail,name="detail"),
    
    path('',views.PositionListView.as_view(),name='position-list'),
    path('create/',views.PositionCreateView.as_view(),name='position-create'),
    path('<int:pk>/',views.PositionDetailView.as_view(),name='position-detail'),
    path('update/<int:pk>',views.PositionUpdateView.as_view(),name='position-update'),
    path('delete/<int:pk>',views.PositionDeleteView.as_view(),name='delete')
   
]
