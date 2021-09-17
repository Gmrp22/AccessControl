from QR.models import access
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from QR.views import *



router = DefaultRouter()
router.register(r'user', user.UserViewSet),
router.register(r'access', access.AccessViewSet),
router.register(r'qr', qr.QRViewSet),
router.register(r'report', report.ReportViewSet),
urlpatterns = [
    path('', include(router.urls)),
]
