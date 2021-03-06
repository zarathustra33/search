from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
# from .models import Article,CandidateInfo,CandidateEdu,CandidateExperience,RequestLog
from django.contrib.auth.decorators import login_required
from .import forms
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Position,Client
# Create your views here.

class PositionListView(ListView):
    model=Position
    # paginate_by=30
    context_object_name='position_list'
    template_name='positions/position_list.html'
    queryset=Position.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PositionListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['clients'] = Client.objects.all()
        return context

class PositionDetailView(DetailView):
    model=Position
    template_name='positions/position_detail.html'
    context_object_name='position'
    # def get_object(self):
    #     id_=self.kwargs.get('id')
    #     return get_object_or_404(Position,id=id_)

class PositionCreateView(CreateView):
    model=Position

    template_name='positions/position_create.html'
    fields=['company','name','location','account_manager','recruiter','tips','description','file']
    context_object_name='form'

class PositionUpdateView(UpdateView): 
    model=Position
    template_name='positions/position_update.html'
    context_object_name='form'
    fields=['name','account_manager','recruiter','tips','description','file']

class PositionDeleteView(DeleteView):
    model=Position
    success_url= reverse_lazy('positions:position-list')
    
