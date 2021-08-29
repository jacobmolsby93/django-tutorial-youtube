"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import (
    login_view,
    logout_view,
    register_view,
)
from article.views import (
    article_create_view,
    article_detail_view,
    article_search_view,
)
from .views import home_view

# article/int:id needs to best last, because it has datatype int.
# otherwise keep in alphabetical order
urlpatterns = [
    path('', home_view),
    path('article/', article_search_view),
    path('article/create/', article_create_view, name="article-create"),
    path('article/<slug:slug>/', article_detail_view, name='article-detail'),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
