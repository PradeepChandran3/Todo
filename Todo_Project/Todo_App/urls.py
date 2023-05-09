from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.Home,name='home'),
    path('delete/<int:taskid>/',views.Delete,name='delete'),
    path('update/<int:id>/',views.Update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]