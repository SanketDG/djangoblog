from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
	posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_list')
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

