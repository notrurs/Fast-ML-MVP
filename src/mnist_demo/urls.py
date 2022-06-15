from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexPage, FormUpload, AjaxDraw, WsDraw


app_name = 'mnist_demo'

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('form_upload/', FormUpload.as_view(), name='form_upload'),
    path('ajax_draw/', AjaxDraw.as_view(), name='ajax_draw'),
    path('ws_draw/', WsDraw.as_view(), name='ws_draw'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
