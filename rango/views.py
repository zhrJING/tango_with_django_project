from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def homepage(requeest):
    return HttpResponse("Homepage"
                        "<br>"
                        "Rango says hey there partner!"
                        "<br/>"
                        "<a href='/rango/'>Index</href>"
                        "<br>"
                        "<a href='/rango/about/'>About</href>")

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'author': "Haowen Li (2327962L)"}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)
