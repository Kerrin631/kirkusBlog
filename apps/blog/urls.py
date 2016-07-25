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
  url(r'^blog/view/(?P<slug>[^\.]+).html/delete', views.delete_post, name='delete_blog_post'),
  url(r'^blog/category/(?P<slug>[^\.]+).html/delete', views.delete_category, name='delete_category'),
  url(r'^blog/view/(?P<slug>[^\.]+).html/update/$', views.update_post, name='nav_to_update_blog_post'),
  url(r'^blog/view/(?P<slug>[^\.]+).html/update/save', views.update_post_save, name='update_blog_post'),
)