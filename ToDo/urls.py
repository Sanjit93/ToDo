
from django.contrib import admin
from django.urls import path, include
from TodoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    # TODO
    path('todo/',include('TodoApp.urls')),
]
