from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('login_landing/', views.LoginLandingView.as_view(), name='login_landing'),
    path('logout_landing/', views.LogoutLandingView.as_view(), name='logout_landing'),
    path('authentication/', include('authentication.urls', namespace='authentication')),
    path('application/', include('application.urls', namespace='application')),
]

if settings.DEBUG: 
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns