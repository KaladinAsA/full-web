from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView,FormView,View
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from .forms import CommentForm
from accounts.models import CustomUser
from .models import Article, Comment

class ArticleList(LoginRequiredMixin, ListView):
    """showing all articles"""
    model = Article
    template_name = 'article_list.html'
    
class CommentGet(DetailView):
    """loading comments"""
    model = Article
    template_name = 'article_detail.html'
    
    def get_context_data(self, **kwargs):
        # showing comment content
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        # get comments with current user
        comments = Comment.objects.filter(article=article).select_related('user')
        context['form'] = CommentForm
        # add commentform to the context
        context['comments'] = comments
        return context
    
class CommentPost(SingleObjectMixin,FormView):
    """saving comments"""
    model = Article
    form_class = CommentForm
    template_name = 'article_detail.html'
    
    def post(self, request, *args, **kwargs):
        self.obj = self.get_object()
        return super().post(request,*args,**kwargs)
    
    def form_valid(self, form):
        # save the comment with the article and logged-in
        comment = form.save(commit=False)
        comment.article = self.obj
        comment.user = self.request.user
        form.save(author=self.request.user, article=self.get_object())
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        # puting comment on associated article
        article = self.get_object()
        return reverse('article_detail', kwargs={'pk': article.pk})
    
class ArticleDetail(LoginRequiredMixin, View):
    """showing article detail contetn with comments"""
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    
class ArticleCreat(LoginRequiredMixin ,CreateView):
    model = Article
    success_url = reverse_lazy('article_list')
    fields = ['title', 'body', 'image']
    template_name = 'article_create.html'
    
    def form_valid(self, form):
        # set author to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ArticleUpdate(
    LoginRequiredMixin, 
    UserPassesTestMixin,
    UpdateView):
    model = Article
    fields = ['title', 'body', 'image']
    template_name = 'article_update.html'
    
    def test_func(self):
        # cheking user is == to author off article
        obj = self.get_object()
        return obj.author == self.request.user
    
class ArticleDelete(
    LoginRequiredMixin, 
    UserPassesTestMixin,
    DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete.html'
    
    def test_func(self):
        # cheking user is == to author off article
        obj = self.get_object()
        return obj.author == self.request.user