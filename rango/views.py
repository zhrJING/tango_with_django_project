from django.shortcuts import render
from django.http import HttpResponse

def homepage(requeest):
    return HttpResponse("Homepage"
                        "<br>"
                        "<a href='/rango/'>Index</href>"
                        "<br>"
                        "<a href='/rango/about/'>About</href>")

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'author': "Zhengren Jing (2327974J)"}
    return render(request, 'rango/about.html', context=context_dict)
