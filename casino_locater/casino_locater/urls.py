from django.conf.urls import include, url
from django.contrib import admin
from casino_finder.views import ListCreateCasinos
from casino_finder.views import ListCreateUser
from casino_finder.views import schema_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'casino_locater.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/profile/', schema_view),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/casinos',ListCreateCasinos.as_view(), name='list_casinos'),
    url(r'api/user',ListCreateUser.as_view(), name='list_user'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
