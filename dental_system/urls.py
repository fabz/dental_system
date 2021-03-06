"""dental_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'homepage.views.index', name='homepage_index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dentists/', include('dentists.urls')),
    url(r'^transactions/', include('transactions.urls')),
    url(r'^treatments/', include('treatments.urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'^vendors/', include('vendors.urls')),
    url(r'^consumables/', include('consumables.urls')),
    url(r'^prices/', include('prices.urls')),
]
