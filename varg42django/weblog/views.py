
from django.shortcuts import render_to_response
from varg42django.weblog.models import Post

# Create your views here.

def latest(request):
	post = Post.objects.order_by('-pubdate')[0]
	if not post:
		pass    # 404
	else:
		return render_to_response('weblog/latest.html', { 'post': post, })


