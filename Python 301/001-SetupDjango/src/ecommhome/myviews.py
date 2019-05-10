from django.http import HttpResponse
from django.shortcuts import render

# define the custom home page 
def myhome(request):
    content = "<html><head><title>My First Django Home</title></head><body><h1>My First Django Home</h1></body></html>"
    return HttpResponse(content)


