"""
URL configuration for classification project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

# urlpatterns = [
    
#     path('admin/', admin.site.urls),
#     path('',views.home_page),
#     path('about',views.about),
#     path('log_in',views.log_in),
#     path('log_in_parameters',views.log_in_parameters)
    # path('log_in_details',views.log_in_details)

# ]

    # path('service_parameters',views.service_parameters),
    # path('profile/', views.profile, name='profile'),



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('sign_in_details',views.sign_in),
    path('log_in_details',views.log_in),
    path('sign_in_parameters',views.sign_details),
    path('log_in_parameters',views.log_in_details),
    path('log_in_details', views.log_in, name='log_in_details'),
    path('service_parameters',views.service_parameters),
    path('profile', views.profile, name='profile'),
    path('with_draw',views.with_draw,name='with_draw'),
    path('amount_with_draw_details',views.amount_with_draw_details),
    path('deposit',views.deposit,name='deposit'),
    path('amount_deposit_details',views.amount_deposit_details),
    path('balance',views.balance,name='balance'),
    
]
