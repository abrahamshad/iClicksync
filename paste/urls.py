from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_paste, name='create_paste'),
    path('code/<str:code>/', views.show_code, name='show_code'),
    path('retrieve/<str:code>/', views.retrieve_paste, name='retrieve_paste'),
    path('search/', views.search_paste, name='search_paste'),
    # path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
