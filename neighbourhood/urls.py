from django.urls import path,include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns=[
    path('',views.index,name='Index'),
    path('my-profile/',views.my_profile, name='my-profile'),
    re_path('user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    path('create/profile',views.create_profile, name='create-profile'),
    path('update/profile',views.update_profile, name='update-profile'),
    path('blog',views.blog, name='blog'),
    path('new/blogpost',views.new_blogpost, name='new-blogpost'), 
    path('view/blog/(\d+)',views.view_blog,name='view_blog'),
    path('businesses',views.businesses, name='businesses'),
    path('new/business',views.new_business, name='new-business'),
    path('health',views.health, name='health'),
    path('authorities',views.authorities, name='authorities'),
    path('notifications',views.notification, name='notifications'),
    path('new/notification',views.new_notification, name='new-notification'),
    path('search/',views.search_results, name='search_results'), 

    path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), {"next_page": '/'}),
    path('accounts/',include('django_registration.backends.one_step.urls')),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)