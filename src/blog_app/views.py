from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from blog.models import BlogPost
#from .forms import ContactForm

def home_page(request):
    qs = BlogPost.objects.all()
    template_name = 'home.html'
    context = {'object_list' : qs}
    return render(request,template_name,context)

