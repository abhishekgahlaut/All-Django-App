from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logged_in/$', views.logged_in, name='logged_in'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'djangologin/login.html', 'redirect_field_name': '/djangologin/logged_in'}),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/djangologin/login'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),

]