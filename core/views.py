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
    """
    Главная страница

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'ladding.html'
    context_object_name = 'list_articles'


class UserListView(ListView):
    """
    Страница профиля пользователя

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'user_page.html'
    context_object_name = 'list_articles'


class ForumListView(ListView):
    """
    Страница формуа с обсуждениями

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'index.html'
    context_object_name = 'list_articles'


class FAQ(ListView):
    """
    Страница FAQ (Frequently Asked Questions)

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'faq.html'
    context_object_name = 'list_articles'


# Instructions
class instr(ListView):
    """
    Страница выбора инструкции

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/pre_instr.html'
    context_object_name = 'list_articles'


class Hard(ListView):
    """
    Страница инструкций сложного уровня понимания

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/hard_instr.html'
    context_object_name = 'list_articles'


class Mid(ListView):
    """
    Страница инструкций среднего уровня понимания

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/mid_instr.html'
    context_object_name = 'list_articles'


class Low(ListView):
    """
    Страница инструкций лёгкого уровня понимания

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/low_instr.html'
    context_object_name = 'list_articles'


class ASUS(ListView):
    """
    Страница инструкции Asus

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/asus.html'
    context_object_name = 'list_articles'


class tplink(ListView):
    """
    Страница инструкции Tp-Link

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/tp-link.html'
    context_object_name = 'list_articles'


class xiaomi(ListView):
    """
    Страница инструкции Xiaomi

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/xiaomi.html'
    context_object_name = 'list_articles'


class mgts(ListView):
    """
    Страница инструкции МГТС

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/mgts.html'
    context_object_name = 'list_articles'


class keenetic(ListView):
    """
    Страница инструкции Keenetic

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/keenetic.html'
    context_object_name = 'list_articles'


class netis(ListView):
    """
    Страница инструкции Netis

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/netis.html'
    context_object_name = 'list_articles'


class micro(ListView):
    """
    Страница инструкции Microtik

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/keenetic.html'
    context_object_name = 'list_articles'


class hyawei(ListView):
    """
    Страница инструкции Huawei

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    """
    model = Articles
    template_name = 'instructions/hyawei.html'
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
    """
    Главная страница (ф-ии)

    :param model: используемая модель
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param context_object_name: название объекта
    :param form_class: используемая форма
    :param success_msg: сообщение для пользователя при опубликовании/обработке комментария
    """
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
    """
    Функция обновления комментария

    :param item: объект комментария
    """
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
    """
    Страница создания инструкции

    :param login_url: URL при входе на страницу создания записи
    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param form_class: используемая форма
    :param success_url: URL при успешном создании
    :param success_msg: сообщение при успешном создании
    """
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
    """
    Страница обновления инструкции

    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param form_class: используемая форма
    :param success_url: URL при успешном обновлении
    :param success_msg: сообщение при успешном обновлении
    """
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
    """
    Страница входа в систему

    :param template_name: название html шаблона
    :param form_class: используемая форма
    :param success_url: URL при успешном обновлении
    """
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    """
    Страница входа в систему

    :param template_name: название html шаблона
    :param model: ForeignKey `django.contrib.auth.models.User`
    :param form_class: используемая форма `RegisterUserForm`
    :param success_url: URL при успешном создании пользователя
    :param success_msg: сообщение при успешном создании пользователя
    """
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
    """
    Страница (кнопка) выхода из системы

    :param next_page: URL перенаправления
    """
    next_page = reverse_lazy('edit_page')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """
    Страница удаления инструкции

    :type model: :class:`django.contrib.auth.models.Articles`
    :param template_name: название html шаблона
    :param success_url: URL при успешном удалении
    :param success_msg: сообщение при успешном удалении
    """
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
