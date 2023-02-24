from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('regi/', views.register, name='register'),
    path('create_post/', views.create_post, name='create_post'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('update/',views.update,name='update'),
    path('<int:id>/like/', views.like_post, name='like_post'),
    path('<int:id>/dislike/', views.dislike_post, name='dislike_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    # path('delete/<int:id>/',views.delete_image, name='delete_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
