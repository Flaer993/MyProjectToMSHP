"""iswork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views



urlpatterns = [
    #core
    path('', views.HomeListView.as_view(), name='home'),
    path('detail/<int:pk>', views.HomeDetailView.as_view(), name='detail_page'),
    path('edit-page', views.ArticleCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.ArticleDeleteView.as_view(), name='delete_page'),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout_page'),
    path('forum', views.ForumListView.as_view(), name='forum'),
    path('faq', views.FAQ.as_view(), name='faq'),
    #Insructions

    path('asus', views.ASUS.as_view(), name='asus'),
    path('tp-link', views.tplink.as_view(), name='tp-link'),
    path('xiaomi', views.xiaomi.as_view(), name='xiaomi'),
    path('mgts', views.mgts.as_view(), name='mgts'),
    path('rosteleckom', views.tplink.as_view(), name='rosteleckom'),
    path('netis', views.tplink.as_view(), name='netis'),
    path('keenetic', views.keenetic.as_view(), name='keenetic'),
    path('hyawei', views.hyawei.as_view(), name='hyawei'),
    path('mickrotik', views.tplink.as_view(), name='mickrotik'),
    #ajax
    path('update_comment_status/<int:pk>/<slug:type>', views.update_comment_status, name='update_comment_status')



]
