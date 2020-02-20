from django.urls import path
from . import views

# path(route, view[, kwargs, name])
# route is string that contains URL pattern. doesn't search GET/POST params ie mysite.com/polls/?page=3
# view calls the function from views.py with an HttpRequest object and any values from the route
# name allows referencing
urlpatterns = [
    path('mypage', views.mypage, name='mypage'),
    path('', views.index, name='index'),
]