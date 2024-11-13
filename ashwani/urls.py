from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from ashwani.common_modules.mainServices import MainService




admin.site.site_title = "Ashwani_Portfolio Admin"
admin.site.site_header = "Ashwani_Portfolio Administration"
admin.site.index_title = "Ashwani_Portfolio Administration"

urlpatterns = [
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


