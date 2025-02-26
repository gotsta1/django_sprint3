from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "blog/index.html"


class PostDetail(TemplateView):
    template_name = "blog/detail.html"


class CategoryPosts(TemplateView):
    template_name = "blog/category.html"
