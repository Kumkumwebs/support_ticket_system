from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 👇 Redirect base URL to dashboard
    path('', lambda request: redirect('dashboard-page')),

    # ✅ This includes both API and dashboard views
    path('', include('dashboard.urls')),  
    
    # ✅ DRF & Django auth
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
