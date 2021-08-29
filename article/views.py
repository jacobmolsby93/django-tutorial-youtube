from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import ArticleForm
from .models import Article


def article_search_view(request):
    query = request.GET.get('query') # this is a dictionary
    qs = Article.objects.search(query=query)
    context = {
        "object_list": qs # search.html object.title...
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
        # context['object'] = article_object # Rinses the form when form created
        # context['created'] = True
        # return redirect("article-detail", slug=article_object.slug)
        return redirect(article_object.get_absolute_url())
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


def article_detail_view(request, slug=None):
    article_obj = None
    if id is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": article_obj,
    }

    return render(
        request,
        "articles/detail.html", 
        context=context
    )