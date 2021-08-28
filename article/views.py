from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ArticleForm
from .models import Article


# Create your views here.

def article_search_view(request):
    print(request.GET)
    query_dict = request.GET # this is a dictionary
    query = query_dict.get('query') # input type="text" name="query"

    try: 
        query = int(query_dict.get('query'))
    except: 
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj # search.html object.title...
    }
    return render(
        request,
        "articles/search.html",
        context=context
    )


@login_required
def article_create_view(request):
    # print(request.POST)
    form = ArticleForm(request.POST or None) # if it is POST data its going to innit if its not its == get
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        # context['form'] = ArticleForm()
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content') # theese 3 lines not required in modelform
        # article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object # Rinses the form when form created
        context['created'] = True
    return render(
        request,
        "articles/create.html", 
        context=context
    )
    
# reference

# def article_create_view(request):
#     # print(request.POST)
#     form = ArticleForm()
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST) # passing in unclean data
#         context['form'] = form # shows the error of ValidationError
#         if form.is_valid(): # if it its valid its == cleaned
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             article_object = Article.objects.create(title=title, content=content)
#             context['object'] = article_object
#             context['created'] = True
#     return render(
#         request,
#         "articles/create.html", 
#         context=context
#     )


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }

    return render(
        request,
        "articles/detail.html", 
        context=context
    )