"""
URL configuration for djangoProject_almamarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from posts import views as post_views
from users import views as user_views
from djangoProject_almamarket import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', post_views.main_view),
    path('posts/', post_views.posts_view),
    path('product/', post_views.product_view),
    path('category/', post_views.category_view),
    path('products/<int:id>/', post_views.product_detail_view),
    path('posts/<int:id>/', post_views.post_detail_view),#
    path('reviews/', post_views.review_view),

    path('posts/create/', post_views.posts_create_view),
    path('product/create/', post_views.product_create_view),
    path('category/create/', post_views.category_create_view),
    path('reviews/create/', post_views.review_create_view),

    path('users/register/', user_views.register_view),
    path('users/auth/', user_views.auth_view),
    path('users/logout/', user_views.logout_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
