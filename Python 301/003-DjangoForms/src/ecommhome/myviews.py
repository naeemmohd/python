from django.http import HttpResponse
from django.shortcuts import render
from .myforms import ContactForm

# define the custom home page 
def myhome(request):
    pageContext = {
        'title': 'My Home Page',
        'mainheader': 'This is a Home page using Context based HTML Templates'
    }
    return render(request, "myhomepage.html", pageContext)

# define the custom contacts page 
def mycontacts(request):
    pageContext = {
        'title': 'My Contacts Page',
        'mainheader': 'This is a Contacts page using Context based HTML Templates'
    }
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('contactname'))
        print(request.POST.get('emailid'))
        print(request.POST.get('address'))
    return render(request, "mycontacts/myview.html", pageContext)

# define the custom aboutus page 
def myaboutus(request):
    formInstance = ContactForm(request.POST or None)
    pageContext = {
        'title': 'My About Us Page',
        'mainheader': 'This is a About Us page using Context based HTML Templates',
        'form' : formInstance
    }
    if formInstance.is_valid():
        print(formInstance.cleaned_data)
    #if request.method == "POST":
    #    print(request.POST)
    #    print(request.POST.get('contactname'))
    #    print(request.POST.get('emailid'))
    #    print(request.POST.get('address'))
    return render(request, "myaboutus/myview.html", pageContext)

def myhome_discarded(request):
    content = """
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

        <title>My First Django App using Inline Templates!</title>
    </head>
    <body>
        <div class="text-center">
            <h1>My First Django App using Inline Templates!</h1>
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
    </html>
    """
    return HttpResponse(content)


