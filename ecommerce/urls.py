from django.conf.urls import url
from django.contrib import admin
from ecommerce import views

urlpatterns = [
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^products/$', views.ProdottoListView.as_view(), name='products'),
    url(r'^products/(?P<prodotto_id>\d*)$', views.prodotto_show, name='prodotto_details'),
    url(r'^new/$', views.prodotto_create, name='prodotto_new'),
    url(r'^edit/(?P<prodotto_id>\d+)$', views.prodotto_update, name='prodotto_edit'),
    url(r'^delete/(?P<prodotto_id>\d+)$', views.prodotto_delete, name='prodotto_delete'),
    url(r'^$', views.index, name='index'),
]
