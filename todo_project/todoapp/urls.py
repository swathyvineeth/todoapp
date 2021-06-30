
from django.urls import path
from.import views
urlpatterns=[

    path('', views.taskview,name='taskview'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('update/<int:id>/', views.update,name='update'),
    path('cobjview/', views.task_view.as_view(), name='cobjview'),
    path('cobjdetailview/<int:pk>/', views.detail_view.as_view(), name='cobjdetailview'),
    path('cobjupdateview/<int:pk>/', views.update_view.as_view(), name='cobjupdateview'),
    path('cobjdeletetask/<int:pk>/', views.delete_task.as_view(), name='cobjdeletetask'),


]

