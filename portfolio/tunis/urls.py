from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path



urlpatterns = [
    path('', show_index, name='index'),
    path('about/', show_about, name='about'),
    path('portfolio/', show_portfolio, name='portfolio'),
    path('contact/', show_contact, name='contact'),
    path('detail/<int:pk>/', show_detail_project, name='detailProject')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)