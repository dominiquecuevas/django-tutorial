from django.urls import path
from . import views

# path(route, view[, kwargs, name])
# route is string that contains URL pattern. doesn't search GET/POST params ie mysite.com/polls/?page=3
# view calls the function from views.py with an HttpRequest object and any values from the route
# name allows referencing

# namespacing to make sure django goes to the right view if apps share the same name
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]