from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplechat.views.home', name='home'),
    # url(r'^simplechat/', include('simplechat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^ask$', 'chat.views.ask', name='ask'),
    url(r'^/?$', 'chat.views.home', name='home'),
    url(r'^feed?$', 'chat.views.feed', name='feed'),
    url(r'^new?$', 'chat.views.newbot', name='newbot'),
    url(r'^interact?$', 'chat.views.interact', name='interract'),
)
