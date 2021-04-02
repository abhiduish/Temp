from django.urls import path,include
from api import views

urlpatterns=[
    path('post/<str:name>/<str:address>/<int:age>/<int:totalmarks>',views.save,name='save'),
    path('get_all',views.get_all,name='get_all'),
    path('get_data/<str:name>',views.get_data,name='get_data'),
    path('delete/<str:name>',views.delete,name='delete'),
    path('filter',views.filter,name='filter')
]