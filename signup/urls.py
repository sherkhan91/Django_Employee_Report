from django.urls import path,include
from signup import views

urlpatterns = [
    path('', views.index, name="index"),
    path('showimage', views.showimage, name='showimage'),
    path('showform', views.showform, name='showform'),
    path('dbtest', views.dbtest, name='dbtest'),
    path('testreturn', views.testreturn, name='testreturn'),
    path('success', views.success, name='success'),
]