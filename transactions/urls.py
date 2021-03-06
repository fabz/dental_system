from django.conf.urls import patterns, url

from transactions.views import TrxIndexView, TrxNewView, TrxEditView, TrxDetailIndexView, TrxDetailNewView, TrxDetailEditView,\
    TrxDetailPrintView


urlpatterns = patterns('',
                       url(r'^$', TrxIndexView.as_view(), name='trxs_index'),
                       url(r'^new/$', TrxNewView.as_view(), name='trxs_new'),
                       url(r'^(?P<pk>\d+)/edit/$', TrxEditView.as_view(), name='trxs_edit'),
                       url(r'^detail/([0-9]*)/$', TrxDetailIndexView.as_view(), name='trxs_detail_index'),
                       url(r'^detail/([0-9]*)/views/$', TrxDetailPrintView.as_view(), name='trxs_detail_view'),
                       url(r'^detail/([0-9]*)/(?P<pk>\d+)/edit/$', TrxDetailEditView.as_view(), name='trxs_detail_edit'),
                       url(r'^detail/new/([0-9]*)/$', TrxDetailNewView.as_view(), name='trxs_detail_new'),
                       #                        url(r'^(?P<pk>\d+)/edit_price/$', EditPriceView.as_view(), name='set_product_price'),
                       #                        url(r'^(?P<pk>\d+)/edit_bonus/$', EditBonusView.as_view(), name='set_product_bonus'),
                       #                        url(r'^(?P<pk>\d+)/toggle_activation/$', ToggleActivationView.as_view(), name='toggle_product_activation'),
                       #                        url(r'^(?P<pk>\d+)/edit_rank/$', EditRankView.as_view(), name='product_edit_rank'),
                       #                        url(r'^(?P<pk>\d+)/delete/$', ProductDeleteView.as_view(), name='delete_product'),
                       #                        #     url(r'^(?P<pk>\d+)/remove/$', product_views.DeleteView.as_view(), name='product_delete'),
                       #

                       )
