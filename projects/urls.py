from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout


from projects.projects import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.projects),

    url(r'^login', login,  {'template_name':'login.html'}, name='login'),
    url(r'^logout', logout, {'next_page':'/'}, name='logout'),

    url(r'^new_project', views.new_project, name='new_project'),
    url(r'^projects/(?P<pk>\d+)/$', views.project),

    url(r'^projects/(?P<pk>\d+)/delete/$', views.ProjectDelete.as_view()),
    url(r'^project_form/(?P<pk>\d+)/$', views.ProjectUpdate.as_view(), name='ProjectUpdate'),
)
