from django.http import HttpResponse
from django.shortcuts import render

# define the custom home page 
def myhome(request):
    return render(request, "myhomepage.html", {})