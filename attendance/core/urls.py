# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import StaffList, StaffDetail, AttendanceList, AttendanceDetail, CustomUserCreate, CustomUserDetail, MarkAttendance

urlpatterns = [
    path('users/', CustomUserCreate.as_view(), name='user-create'),
    path('users/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),
    path('staff/', StaffList.as_view(), name='staff-list'),
    path('staff/<int:pk>/', StaffDetail.as_view(), name='staff-detail'),
    path('attendance/', AttendanceList.as_view(), name='attendance-list'),
    path('attendance/<int:pk>/', AttendanceDetail.as_view(), name='attendance-detail'),
    path('mark-attendance/', MarkAttendance.as_view(), name='mark-attendance'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Map media URLs
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
