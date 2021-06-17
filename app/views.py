from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic 
from .forms import EmailPostForm
from django.core.mail import send_mail
# Create your views here.

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'


  def post_share(request, post_id):
# Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
# Form was submitted
      form = EmailPostForm(request.POST)
      if form.is_valid():
# Form fields passed validation
        cd = form.cleaned_data
        post_url = request.build_absolute_uri(
        post.get_absolute_url())
        subject = '{} ({}) recommends you reading {}"'.format(cd['name'], cd['email'], post.title)
        message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
        send_mail(subject, message, 'admin@myblog.com',
 [cd['to']])
      sent = True
    else:
     form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,'form': form,'sent': sent})

