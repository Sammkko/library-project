from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from libraries.decorators import allowed_users, admin_only

# Create your views here.

def news(request):
    posts = News.objects.all()
    postlar = Paginator(posts, 6)
    page_list = request.GET.get('page')
    page = postlar.get_page(page_list)
    context = {'posts': page, }
    return render(request, 'news.html', context)


def newsOnly(request, pk):
    post = News.objects.get(id=pk)
    post.news_view = post.news_view + 1
    post.save()
    posts = News.objects.all().order_by('-create_date')[0:6]
    context = {'post': post, 'posts': posts}
    return render(request, 'newsOnly.html', context)


@login_required(login_url='login')
@admin_only
def deletePost(request, pk):
    item = News.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'deletepost.html', context)


@login_required(login_url='login')
@admin_only
def updatePost(request, pk):
    news_task = News.objects.get(id=pk)

    form = NewsForm(instance=news_task)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_task)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}

    return render(request, 'updatepost.html', context)


@login_required(login_url='login')
@admin_only
def createPost(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'createpost.html', context)
