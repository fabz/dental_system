from django.conf.urls import patterns, url

from consumables.views import *


urlpatterns = patterns('',
                       url(r'^$', ConsumablesIndexView.as_view(), name='consumables_index'),
                       url(r'^new/$', ConsumablesNewView.as_view(), name='consumables_new'),
                       url(r'^(?P<pk>\d+)/edit/$', ConsumablesEditView.as_view(), name='consumables_edit'),
                       url(r'^(?P<pk>\d+)/mutation_new/$', ConsumablesMutationNewView.as_view(), name='mutation_new'),
                       url(r'^(?P<pk>\d+)/mutation_hist/$', ConsumablesMutationHistView.as_view(), name='mutation_hist'),
                       #url(r'^stockin/(?P<pk>\d+)/edit/$', ConsumablesStockinEditView.as_view(), name='stockin_edit'),
                       #                        url(r'^(?P<pk>\d+)/edit/$', EditView.as_view(), name='product_edit'),
                       #                        url(r'^(?P<pk>\d+)/edit_price/$', EditPriceView.as_view(), name='set_product_price'),
                       #                        url(r'^(?P<pk>\d+)/edit_bonus/$', EditBonusView.as_view(), name='set_product_bonus'),
                       #                        url(r'^(?P<pk>\d+)/toggle_activation/$', ToggleActivationView.as_view(), name='toggle_product_activation'),
                       #                        url(r'^(?P<pk>\d+)/edit_rank/$', EditRankView.as_view(), name='product_edit_rank'),
                       #                        url(r'^(?P<pk>\d+)/delete/$', ProductDeleteView.as_view(), name='delete_product'),
                       #                        #     url(r'^(?P<pk>\d+)/remove/$', product_views.DeleteView.as_view(), name='product_delete'),
                       #

                       )
