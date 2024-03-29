from django.shortcuts import render, redirect, HttpResponse

from .models import Articles, Comments
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .forms import ArticleForm, AuthUserForm, RegisterUserForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from . import views

from django.template import Context, Template




class HomeListView(ListView):
    model = Articles
    template_name = 'ladding.html'
    context_object_name = 'list_articles'
class UserListView(ListView):
    model = Articles
    template_name = 'user_page.html'
    context_object_name = 'list_articles'

class ForumListView(ListView):
    model = Articles
    template_name = 'index.html'
    context_object_name = 'list_articles'


class FAQ(ListView):
    model = Articles
    template_name = 'faq.html'
    context_object_name = 'list_articles'

#Instructions type
class instr(ListView):
    model = Articles
    template_name = 'instructions/pre_instr.html'
    context_object_name = 'list_articles'

class Hard(ListView):
    model = Articles
    template_name = 'instructions/hard_instr.html'
    context_object_name = 'list_articles'
    
class Mid(ListView):
    model = Articles
    template_name = 'instructions/mid_instr.html'
    context_object_name = 'list_articles'

class Low(ListView):
    model = Articles
    template_name = 'instructions/low_instr.html'
    context_object_name = 'list_articles'
#inst Hards
class ASUS(ListView):
    model = Articles
    template_name = 'instructions/asus.html'
    context_object_name = 'list_articles'

class tplink(ListView):
    model = Articles
    template_name = 'instructions/tp-link.html'
    context_object_name = 'list_articles'

class rostelecom(ListView):
    model = Articles
    template_name = 'instructions/rostelecom.html'
    context_object_name = 'list_articles'

class xiaomi(ListView):
    model = Articles
    template_name = 'instructions/xiaomi.html'
    context_object_name = 'list_articles'

class mgts(ListView):
    model = Articles
    template_name = 'instructions/mgts.html'
    context_object_name = 'list_articles'

class keenetic(ListView):
    model = Articles
    template_name = 'instructions/keenetic.html'
    context_object_name = 'list_articles'

class netis(ListView):
    model = Articles
    template_name = 'instructions/netis.html'
    context_object_name = 'list_articles'

class micro(ListView):
    model = Articles
    template_name = 'instructions/keenetic.html'
    context_object_name = 'list_articles'

class hyawei(ListView):
    model = Articles
    template_name = 'instructions/hyawei.html'
    context_object_name = 'list_articles'
#inst Mid

class ASUSmid(ListView):
    model = Articles
    template_name = 'instructions/inst_mid/asus_mid.html'
    context_object_name = 'list_articles'

class tplinkMid(ListView):
    model = Articles
    template_name = 'instructions/inst_mid/tp-link_mid.html'
    context_object_name = 'list_articles'

class rostelecomMid(ListView):
    model = Articles
    template_name = 'instructions/inst_mid/rostelecom_mid.html'
    context_object_name = 'list_articles'

class xiaomiMid(ListView):
    model = Articles
    template_name = 'instructions/inst_mid/xiaomi_mid.html'
    context_object_name = 'list_articles'

class mgtsMid(ListView):
    model = Articles
    template_name = 'instructions/inst_mid/mgts_mid.html'
    context_object_name = 'list_articles'

class keeneticMid(ListView):
    model = Articles
    template_name = 'instructions/inst_mid/keenetic_mid.html'
    context_object_name = 'list_articles'

class netisMid(ListView):
    model = Articles
    template_name = 'instructions/inst_mid/netis_mid.html'
    context_object_name = 'list_articles'

class microMid(ListView):
    model = Articles
    template_name = 'instructions/inst_mid/mickrotik_mid.html'
    context_object_name = 'list_articles'

class hyaweiMid(ListView):
    model = Articles
    template_name = 'instructions/inst_mid/hyawei_mid.html'
    context_object_name = 'list_articles'

#inst low
class hyaweiLow(ListView):
    model = Articles
    template_name = 'instructions/inst_low/hyawei_low.html'
    context_object_name = 'list_articles'

class ASUSlow(ListView):
    model = Articles
    template_name = 'instructions/inst_low/asus_low.html'
    context_object_name = 'list_articles'

class tplinkLow(ListView):
    model = Articles
    template_name = 'instructions/inst_low/tp-link_low.html'
    context_object_name = 'list_articles'

class rostelecomLow(ListView):
    model = Articles
    template_name = 'instructions/inst_low/rostelecom_low.html'
    context_object_name = 'list_articles'

class xiaomiLow(ListView):
    model = Articles
    template_name = 'instructions/inst_low/xiaomi_low.html'
    context_object_name = 'list_articles'

class mgtsLow(ListView):
    model = Articles
    template_name = 'instructions/inst_low/mgts_low.html'
    context_object_name = 'list_articles'

class keeneticLow(ListView):
    model = Articles
    template_name = 'instructions/inst_low/keenetic_low.html'
    context_object_name = 'list_articles'

class netisLow(ListView):
    model = Articles
    template_name = 'instructions/inst_low/netis_low.html'
    context_object_name = 'list_articles'

class microLow(ListView):
    model = Articles
    template_name = 'instructions/inst_low/mickrotik_low.html'
    context_object_name = 'list_articles'



# class LoginRequiredMixin(AccessMixin):
#     """Verify that the current user is authenticated."""
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)

class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class HomeDetailView(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'get_article'
    form_class = CommentForm
    success_msg = 'Комментарий успешно создан, ожидайте модерации'

    def get_success_url(self):
        return reverse_lazy('detail_page', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def update_comment_status(request, pk, type):
    item = Comments.objects.get(pk=pk)
    if request.user != item.article.author:
        return HttpResponse('deny')

    if type == 'public':
        import operator
        item.status = operator.not_(item.status)
        item.save()
        template = 'comment_item.html'
        context = {'item': item, 'status_comment': 'Комментарий опубликован'}
        return render(request, template, context)

    elif type == 'delete':
        item.delete()
        return HttpResponse('''
        <div class="alert alert-success">
        Комментарий удален
        </div>
        ''')

    return HttpResponse('1')


class ArticleCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Articles
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись создана'

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Articles.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Articles
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись успешно обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid



class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('edit_page')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    template_name = 'edit_page.html'
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
