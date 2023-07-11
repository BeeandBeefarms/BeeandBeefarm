"""
URL configuration for project_done project.

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
from application import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing_page/',views.landing_page),
    # path('log_in_page/',views.log_in_page),
    # path('order_sts_page/',views.order_sts_page),
    # path('buy_sell_page/',views.buy_sell_page),
    # path('order_sts_main_page/',views.order_sts_main_page),
    # path('sign_up_page/',views.sign_up_page),
]

