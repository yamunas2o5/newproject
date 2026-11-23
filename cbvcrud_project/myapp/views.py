from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from myapp.models import student
from django.urls import reverse_lazy

# Create your views here.
class StudentList(ListView):
    model=student   
    #default templates = student_list.html
    #default context = student_list

class StudentDetail(DetailView):
    model=student
    #default templates = student_detail.html
    #default context = student

class StudentUpdate(UpdateView):
    model=student
    fields='__all__'
   
    #default templates = student_form.html
    #default context = form

class StudentDelete(DeleteView):
    model=student
    success_url=reverse_lazy('studentlist')
    #sucess_url is used to display the target page
    #default templates=student_confirm_delete.html
    #default context=student

class StudentCreate(CreateView):
    model=student
    fields='__all__'
    
    #default templates = student_form.html
    #default context = form