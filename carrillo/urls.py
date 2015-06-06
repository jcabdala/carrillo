from django.conf.urls import patterns, include, url
from django.contrib import admin
from encuestas.views import ContactView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carrillo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^encuesta/', "encuestas.views.encuesta", name="encuesta"),
    url(r'^encuesta/$', ContactView.as_view()),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',name="my_login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),
)
