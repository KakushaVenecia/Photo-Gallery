from django.urls import include,re_path as url
# from . import views
from django.conf import settings
from django.conf.urls.static import static

from gallery import views

urlpatterns=[
    url('^$',views.index, name = 'index'),
    url('^mygallery/$', views.mygallery, name='mygallery'),
    url('^mygallery/(\d+)/', views.mygallery_details, name='mygallery_details'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^category/(\d+)', views.category,name = 'category')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)