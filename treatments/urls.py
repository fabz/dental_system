from django.conf.urls import patterns, url

from treatments.views import TreatmentsIndexView, TreatmentsNewView,\
    TreatmentsEditView, TreatmentsEditPriceView


urlpatterns = patterns('',
                       url(r'^$', TreatmentsIndexView.as_view(), name='treatments_index'),
                       url(r'^new/$', TreatmentsNewView.as_view(), name='treatments_new'),
                       url(r'^(?P<pk>\d+)/edit/$', TreatmentsEditView.as_view(), name='treatments_edit'),
                       url(r'^(?P<pk>\d+)/edit_prices/$', TreatmentsEditPriceView.as_view(), name='treatments_price_edit'),
                       #                        url(r'^(?P<pk>\d+)/edit_price/$', EditPriceView.as_view(), name='set_product_price'),
                       #                        url(r'^(?P<pk>\d+)/edit_bonus/$', EditBonusView.as_view(), name='set_product_bonus'),
                       #                        url(r'^(?P<pk>\d+)/toggle_activation/$', ToggleActivationView.as_view(), name='toggle_product_activation'),
                       #                        url(r'^(?P<pk>\d+)/edit_rank/$', EditRankView.as_view(), name='product_edit_rank'),
                       #                        url(r'^(?P<pk>\d+)/delete/$', ProductDeleteView.as_view(), name='delete_product'),
                       #                        #     url(r'^(?P<pk>\d+)/remove/$', product_views.DeleteView.as_view(), name='product_delete'),
                       #

                       )
