from django.urls import path

from article.views import (
    article_create_view,
    article_detail_view,
    article_search_view,
)

app_name = 'article'
urlpatterns = [
    path('', article_search_view, name='search'),
    path('create/', article_create_view, name='create'),
    path('<slug:slug>/', article_detail_view, name='detail'),
]