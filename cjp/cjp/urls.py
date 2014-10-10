from django.conf.urls import patterns, include, url

from django.conf import settings

from django.conf.urls.static import static

from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cjp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'signups.views.home', name='home'),
    url(r'^signup-success/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^about-us/$', 'signups.views.about', name='about'),
    #url(r'^logged-in/$', 'signups.views.login', name='login'),
    #url(r'^authenticating/$', 'signups.views.authentication', name='authentication'),
    #url(r'^authentication-failed/$', 'signups.views.invalid_login', name='AuthenticationFailed'),

    url(r'^logged-in/$', 'signups.views.logged', name='logged'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
