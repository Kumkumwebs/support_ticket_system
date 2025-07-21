from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token

#  Custom homepage view
def home_view(request):
    return HttpResponse(" Support Ticket System API is running.<br>Use /api/ for tickets and /api-token-auth/ to get token.")

urlpatterns = [
    path('', home_view),  # Homepage route
    path('admin/', admin.site.urls),
    path('api/', include('tickets.urls')),
    path('api-token-auth/', obtain_auth_token),
]
