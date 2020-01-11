from django.shortcuts import render, get_object_or_404

# add reference for ListView and DetailView
from django.views.generic import ListView, DetailView
from .models import Student

# Create your views here.
# Please note that this one is the first "class" based view as until now we havd been creating function based views

# class based view
class StudentListView(ListView):
    # this is one liner which all you need
    #querySet = Student.objects.all()
    template_name= "student/student_listview.html"

    # Every Django view class will have this method to get the context data
    def get_context_data(self, *args, **kwargs):
        # function to get the contect data
        context = super(StudentListView, self).get_context_data(*args, **kwargs)
        print(context)
        # Incase you need to update the context by adding a few more keys
        context['vw_type'] = "Class based list view"
        return context
 
    # function to get the queryset
    def get_queryset(self):
        return Student.objects.all()

#function based view

# has you written a function based view it would have been something like below
# The class based view above is 1 liner and the function based view below is 5 liner
def Student_ListView(request):
    querySet = Student.objects.all()
    context = {
        'vw_type': "Function based list view",
        'qs' : querySet
    }
    print(context)
    return render(request, "student/student_listview.html", context)


#class based view
class StudentDetailView(DetailView):
    # this is one liner which all you need
    querySet = Student.objects.all()
    template_name= "student/student_detailview.html"

    # Every Django view class will have this method to get the context data
    def get_context_data(self,*args, **kwargs):
        context = super(StudentDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        context['vw_type'] = "Class based detail view"
        return context
 
    def get_queryset(self):
        return Student.objects.all()


# function based view
def Student_DetailView(request, pk=None, *args, **kwargs):
    #objStud = Student.objects.get(id=pk)
    objStud = get_object_or_404(Student, pk=pk)
    context = {
        'vw_type': "Function based detailview",
        'object' : objStud
    }
    print(context)
    return render(request, "student/student_detailview.html", context)