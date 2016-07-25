from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^blog/view/(?P<slug>[^\.]+).html/$', views.view_post, name='view_blog_post'),
  url(r'^blog/category/(?P<slug>[^\.]+).html/$', views.view_category, name='view_blog_category'),
  url(r'^blog/create_new_category/$', views.new_category, name='create_new_category'),
  url(r'^blog/create_new_category/addCategory', views.addCategory, name='addCategory'),
  url(r'^blog/create_new_post/$', views.new_post, name='create_new_post'),
  url(r'^blog/create_new_post/addPost', views.addPost, name='addPost'),
)