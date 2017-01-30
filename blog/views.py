from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render (request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	Post.objects.get(pk=pk)
	posts = get_object_or_404(Post, pk=pk)
	template =('blog/post_detail.html')
	data ={'post': posts, 'teguh': "teguh"}
	print( data['post'] )
	return render (request,template , data)