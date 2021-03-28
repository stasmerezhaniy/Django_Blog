
from django.shortcuts import *
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import *



def index(request):
    latest_article_list = Article.objects.all().order_by('-id')
    paginator = Paginator(latest_article_list, 3)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'articles/listAllPosts.html', {"latest_article_list": contacts})


def detail(requests, articles_id):

    try:
        a = Article.objects.get(id=articles_id)
    except:
        raise Http404("Статья не найдена!")
    latest_comment_list = a.comment_set.all().order_by('-id')
    paginator = Paginator(latest_comment_list, 3)

    page = requests.GET.get('page')
    try:
        cont = paginator.page(page)
    except PageNotAnInteger:
        cont = paginator.page(1)
    except EmptyPage:
        cont = paginator.page(paginator.num_pages)
    return render(requests, 'articles/detail.html', {'articles': a, 'latest_comment_list':cont})


def leave_comment(request, articles_id):

    try:
        a = get_object_or_404(Article, pk=articles_id)
    except:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))







