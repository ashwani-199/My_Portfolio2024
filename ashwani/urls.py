from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from ashwani.common_modules.mainServices import MainService
from django.views.generic.base import TemplateView

from .sitemaps import StaticViewSitemap 
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
}

admin.site.site_title = "Ashwani_Portfolio Admin"
admin.site.site_header = "Ashwani_Portfolio Administration"
admin.site.index_title = "Ashwani_Portfolio Administration"

urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('dashboard/', admin.site.urls),
    path('', include('users.urls')),
]


handler404 = MainService.error_404
handler500 = MainService.error_500
handler403 = MainService.error_403
handler400 = MainService.error_400



if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

if settings.DEBUG == False:
    urlpatterns += staticfiles_urlpatterns()


