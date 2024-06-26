from django.urls import path
from . import views

app_name='post'


urlpatterns = [
  path('', views.home, name='home'),
#  path('list/', views.list, name="list"),
  path('<int:id>/', views.detail, name="detail"),
  path('create/<slug:slug>/', views.create, name="create"),
  path('update/<int:id>/', views.update, name="update"),
  path('delete/<int:id>/', views.delete, name='delete'),
  path('<int:id>/comment_create/', views.com_create, name="com_create"),
  path('<int:post_id>/comment_delete/<int:com_id>/', views.com_delete, name="com_delete"),
  path('<int:post_id>/like', views.post_like, name="post_like"),
  path('<int:post_id>/scrap', views.post_scrap, name="post_scrap"),
  path('<slug:slug>/', views.category_post_list, name="category_post_list"),

]