from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/<str:title>', views.wiki, name='wiki'),
    path('search', views.search, name='search'),
    path('new_entry', views.new_entry, name='new_entry'),
    path('random_entry', views.random_entry, name='random_entry'),
    path('edit', views.edit, name='edit')
]
