from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from .forms import LoginForm

urlpatterns = patterns('accounts.views',
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^register/$', 'register', name='register'),
    # url(r'^settings/$', 'settings', name='settings'),
    url(r'^profile/(?P<user_id>\d+)/$', 'profile', name='profile'),
    # url(r'^password/set/$','set_password'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'home.html', 'next_page': '/login/'}, name='logout'),
)
