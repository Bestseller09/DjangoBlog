from django.shortcuts import render
from blog.models import BlogPost
from .models import SearchQuery

# Create your views here.
def search_view(request):
    query = request.GET.get('q', None)  #request.Get is a dictionary
    user = None
    if request.user.is_authenticated:
        user = request.user
    
    context = {"query":query}
        
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        print(blog_list)
        context['blog_list'] = blog_list
    return render(request,'searches/view.html',context)