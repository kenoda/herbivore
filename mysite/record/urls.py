from django.conf.urls import url, include

from . import views

app_name = 'record'
urlpatterns = [
    # ex: /user/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex:/user
    # url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
    url(r'^plant/$', views.plant_list, name='plant_list'),
    url(r'^plant/add/$', views.plant_edit, name='plant_new'),
    url(r'^plant/edit/plant-(?P<plant_id>\d+)/$', views.plant_edit, name='plant_edit'),
    url(r'^plant/del/plant-(?P<plant_id>\d+)/$', views.plant_del, name='plant_del'),
    # url(r'^plant/detail/plant-(?P<plant_id>\d+)/$', views.ResultsView.as_view(), name='detail'),

    url(r'^plant/(?P<plant_id>\d+)/post/$', views.PostList.as_view(), name='post_list'),
    url(r'^plant/(?P<plant_id>\d+)/add/$', views.post_edit, name='post_new'),
    url(r'^plant/(?P<plant_id>\d+)/(?P<post_id>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^plant/(?P<plant_id>\d+)/(?P<post_id>\d+)/del/$', views.post_del, name='post_del'),
    # url(r'^plant/(?P<plant_id>\d+)/drafts/$', views.post_draft_list, name='post_draft_list'),
    # url(r'^plant/(?P<plant_id>\d+)/publish/$', views.post_publish, name='post_publish'),
]
