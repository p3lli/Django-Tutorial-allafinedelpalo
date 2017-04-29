from django.conf.urls import url
from django.contrib import admin
from ecommerce import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^products/$', views.ProductListView.as_view(), name='products'),
    url(r'^products/(?P<product_id>\d*)$', views.product_show, name='product_show'),
    url(r'^new$', views.product_create, name='product_new'),
    url(r'^edit/(?P<product_id>\d+)$', views.product_update, name='product_edit'),
    url(r'^delete/(?P<product_id>\d+)$', views.product_delete, name='product_delete'),
]
