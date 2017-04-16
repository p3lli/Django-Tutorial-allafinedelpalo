from django.conf.urls import url
from django.contrib import admin
from ecommerce import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^products/$', views.ProdottoListView.as_view(), name='products'),
    url(r'^products/(?P<prodotto_id>[0-9]+)$', views.get_prodotto, name='prodotto_details'),
]
