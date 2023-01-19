from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from user.models import *
# Create your views here.
def begen(request):
    postId = request.POST['postId']
    post = Post.objects.get(id = postId)
    # İşlem yapılabilmesi için kullanıcı girişli olması gerekiyor.
    if request.user.is_authenticated:
            # Hangisine bastığını algılamak için
            if 'begen' in request.POST:
                # Aynı kullanıcı daha öncesinde beğenmiş mi onu kontrol etmek için
                if Post.objects.filter(like__in = [request.user], id = postId).exists():
                    post.like.remove(request.user)
                    post.save()
                    return redirect('index')
                else:
                    post.like.add(request.user)
                    post.dislike.remove(request.user)
                    post.save()
                    return redirect('index')
            if 'begenme' in request.POST:
                if Post.objects.filter(dislike__in = [request.user], id = postId).exists():
                    post.dislike.remove(request.user)
                    post.save()
                else:
                    post.dislike.add(request.user)
                    post.like.remove(request.user)
                    post.save()
            if 'paylas' in request.POST:
                if Post.objects.filter(retweet__in = [request.user], id = postId).exists():
                    post.retweet.remove(request.user)
                    post.save()
                else:
                    post.retweet.add(request.user)
                    post.save()
def index(request):
    if request.user.is_authenticated:
        posts = Hesap.objects.filter(takipci__in = [request.user])
    else:
        posts = Post.objects.all().order_by('-created_at')
    # Gelen post methodu için
    if request.method == 'POST':
        begen(request)
        return redirect('index')
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def olustur(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit= False)
            post.owner = request.user
            post.save()
            messages.success(request, 'Post oluşturuldu')
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'olustur.html', context)

def kesfet(request):
    posts = Post.objects.all().order_by('?')
    if request.method =='POST':
        begen(request)
        return redirect('kesfet')

    context = {
        'posts' : posts
    }
    return render(request, 'kesfet.html', context)