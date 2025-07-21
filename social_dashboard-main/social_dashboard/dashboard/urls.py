from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, dashboard_page, register, update_profile, update_social_accounts

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'posts', PostViewSet)  # ✅ This must be active
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),                         # /api/posts/ and /api/comments/
    path('dashboard/', dashboard_page, name='dashboard-page'),  # /dashboard/
    path('', dashboard_page),
    path('accounts/register/', register, name='register'),
    path('profile/update/', update_profile, name='update-profile'),
    path('accounts/social/', update_social_accounts, name='update-social'),
    path('accounts/', include('django.contrib.auth.urls')),     # login, logout, etc.
]

# ✅ Serve media files (images/videos)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
