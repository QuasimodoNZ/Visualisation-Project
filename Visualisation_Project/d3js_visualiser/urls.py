from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Visualisation_Project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.some_view),
#     url(r'^', 'django.views.generic.simple.direct_to_template', {'template': 'd3js_visualiser/index.html'}),
]
