from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'Visualisation_Project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('d3js_visualiser.urls')),
]
