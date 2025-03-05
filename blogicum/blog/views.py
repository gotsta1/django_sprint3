from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Category
import datetime as dt


class HomePage(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        queryset = Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=dt.datetime.now()
        ).order_by('-pub_date')[:5]
        return queryset


class PostDetail(DetailView):
    template_name = "blog/detail.html"
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(
            Post,
            id=self.kwargs['pk'],
            is_published=True,
            category_id__is_published=True,
            pub_date__lte=dt.datetime.now()
        )


class CategoryPosts(ListView):
    template_name = "blog/category.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = {}
        category_slug = self.kwargs['pk']
        context['post_list'] = get_list_or_404(
            Post,
            category_id__slug=category_slug,
            is_published=True
        )
        context['category'] = get_object_or_404(
            Category,
            slug=category_slug,
            is_published=True
        )
        return context
