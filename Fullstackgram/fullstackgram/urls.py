from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#Modulos

from user import views as users_views
from posts import views as posts_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', users_views.login_views, name='login' ),
    path('feed/', posts_views.feed_view, name='feed' ),
    path('logout', users_views.logout_view, name='logout' ),
    path('register', users_views.register, name='register')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
