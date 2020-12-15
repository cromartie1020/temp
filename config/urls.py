from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Cromartie\'s project'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration' 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('html_format/', include('html_format.urls')),
    path('travel/',include('travel.urls')),
]

if settings.DEBUG: # new
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)