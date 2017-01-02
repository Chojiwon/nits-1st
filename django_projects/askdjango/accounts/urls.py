from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login', kwargs={
        'template_name': 'accounts/login_form.html',
        'authentication_form': LoginForm,
    }),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={
        'next_page': '/',  #'login',
    }),
    url(r'^profile/$', views.profile, name='profile'),
]

