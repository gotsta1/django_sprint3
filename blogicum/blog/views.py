from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    last_posts = Post.objects.select_related('category').filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': last_posts})


def post_detail(request, id):
    post = Post.objects.select_related('category').filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
        pk=id,
    ).first()
    if not post:
        raise Http404()
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category_queryset = Post.objects.select_related('category').filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
        category__slug=category_slug,
    ).order_by('-pub_date')
    print(category_queryset.query)
    if not category_queryset:
        raise Http404()
    category = get_object_or_404(Category, slug=category_slug)
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': category_queryset}
    )
