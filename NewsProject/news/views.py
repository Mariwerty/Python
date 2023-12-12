from django.views.generic import TemplateView, FormView
from news.models import News
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic.base import View

app_url = "/news/"


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by("-created_at")
        return context


class ArticleDetailView(TemplateView):
    template_name = "article_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = News.objects.get(pk=kwargs.get("pk"))
        return context


class RegisterFormView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = app_url + 'login/'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = app_url

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.user = None

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)
