from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name="index"),
    path('html_tag_scrapping', views.HtmlTagScrap, name="html_tag_scrap")
]