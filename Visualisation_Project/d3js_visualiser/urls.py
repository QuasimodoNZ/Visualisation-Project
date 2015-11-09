from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Visualisation_Project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'choropleth-country/', views.choropleth_country),
    url(r'choropleth-state/', views.choropleth_state),
    url(r'chord-country/', views.chord_country),
    url(r'chord-state/', views.chord_state),
    url(r'bar-country/', views.bar_country),
    url(r'bar-state/', views.bar_state),
    url(r'force-country/', views.force_country),
    url(r'force-state/', views.force_state),
#     url(r'^', 'django.views.generic.simple.direct_to_template', {'template': 'd3js_visualiser/index.html'}),
]
