from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # The urls patterns of the blog
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
]
