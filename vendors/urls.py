from django.conf.urls import patterns, url

from vendors.views import *


urlpatterns = patterns('',
                       url(r'^$', VendorsIndexView.as_view(), name='vendors_index'),
                       url(r'^new/$', VendorsNewView.as_view(), name='vendors_new'),
                       url(r'^(?P<pk>\d+)/edit/$', VendorsEditView.as_view(), name='vendors_edit'),
                       #                        url(r'^(?P<pk>\d+)/edit/$', EditView.as_view(), name='product_edit'),
                       #                        url(r'^(?P<pk>\d+)/edit_price/$', EditPriceView.as_view(), name='set_product_price'),
                       #                        url(r'^(?P<pk>\d+)/edit_bonus/$', EditBonusView.as_view(), name='set_product_bonus'),
                       #                        url(r'^(?P<pk>\d+)/toggle_activation/$', ToggleActivationView.as_view(), name='toggle_product_activation'),
                       #                        url(r'^(?P<pk>\d+)/edit_rank/$', EditRankView.as_view(), name='product_edit_rank'),
                       #                        url(r'^(?P<pk>\d+)/delete/$', ProductDeleteView.as_view(), name='delete_product'),
                       #                        #     url(r'^(?P<pk>\d+)/remove/$', product_views.DeleteView.as_view(), name='product_delete'),
                       #

                       )
