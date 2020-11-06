from django.urls import path
from login import views 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name="index"),
    path('logout_request', views.logout_request, name="logout"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('user_home', views.user_home, name="user_home"),
    path('user_leave', views.user_leave, name="user_leave"),
    path('user_editprofile', views.user_editprofile, name="user_editprofile"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('admin_feedback', views.admin_feedback, name="admin_feedback"),
    path('admin_leaves', views.admin_leaves, name="admin_leaves"),
    path('admin_users', views.admin_users, name="admin_users"),
    path('admin_lazyusers', views.admin_lazyusers, name="admin_lazyusers"),
    path('admin_addemployee', views.admin_addemployee, name="admin_addemployee"),
    path('checkdatabase', views.checkdatabase, name="checkdatabase"),
    path('profileimg', views.profileimg, name="profileimg"),
 
    
    # path('profile/<int:year>/', views.profile, name="profile"),
    # path('profile/<int:year>/<str:strr>', views.profile, name="profile"),
    # path('profile/', views., name="profile"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)