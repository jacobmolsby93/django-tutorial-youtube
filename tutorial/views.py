"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from article.models import Article


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the reponse)
    """

    
    article_obj = Article.objects.get()  
    article_queryset = Article.objects.all()
    random_id = random.randint(1, 4)
    # article_title = article_obj.title
    # article_content = article_obj.content

    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }
    # tmpl = get_template('home-view.html')
    # tmpl_string = tmpl.render(context=context)

    HTML_STRING = render_to_string('home-view.html', context=context)
    
    # HTML_STRING = """
    # <h1>{title} (id{id})</h1>

    # <p>{content}</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)