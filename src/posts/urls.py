from django.urls import path, re_path

from . import views

app_name="posts"

urlpatterns = [
    path('create/', views.post_create, name="create"),
    path('<int:id>/delete/', views.post_delete, name="delete"),
    path('<int:id>/edit/', views.post_update, name="update"),
    path('', views.post_list, name="list"),
    path('<int:id>/', views.post_detail, name="detail"),
    path('contact/', views.contact, name="contact"),
    # re_path(r'^detail/(?P<id>[0-9]{1})/$', views.post_detail),
]
