"""wrona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from kruk.views import (
    AddKrukView,
    KrukView,
    MainInaczej,
    RegisterView,
    AddKrukCommentView)
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^$', MainInaczej.as_view(), name="main"),
    path('kruk/<int:pk>', KrukView.as_view(), name="detail"),
    path('kruk/<int:pk>/add', AddKrukCommentView.as_view(), name="add-comment"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register$', RegisterView.as_view(), name='register'),
    url('^add_kruk', AddKrukView.as_view(), name='add-kruk'),
]
