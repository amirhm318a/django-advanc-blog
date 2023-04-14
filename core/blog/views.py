from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView,FormView,CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView,DeleteView
from django.shortcuts import get_object_or_404
from .forms import PostForm

# Create your views here.

# function Base View show a template
'''
def indexView(request):
    return render(request, 'index.html')
'''
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context


class RedirectToMaktab(RedirectView):
    url = 'http://maktabkhooneh.com/'

    def get_redirect_url(self, *args, **kwargs ):
        return super().get_redirect_url(*args, **kwargs)
    

class PostListView(LoginRequiredMixin,ListView):
    # queryset = Post.objects.all()
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = "-id"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=1)
    #     return posts


class PostDetailView(DetailView): 
    model = Post

'''
class PostCreateView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''

class PostCreateView(CreateView):
    model = Post
    # fields = ('author','title','content','status','category','published_date')
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"