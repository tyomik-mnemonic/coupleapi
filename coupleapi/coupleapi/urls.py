"""coupleapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


from dynamic_raw_id.admin import DynamicRawIDMixin


from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework import routers


from lists.views import *
from bid.views import *

#1. API для подключение партнеров, через которое партнер может выполнять действия с анкетами:
#- получение списка анкет (с сортировкой и фильтрами)
#- получение списка подходящих предложений
#- просмотр анкеты по id
#- создание анкеты
#- отправка заявки в кредитные организации (во все или по выбору)

#2. API для кредитных организаций, через которое можно выполнить:
#- получение списка заявок (с сортировкой и фильтрами)
#- просмотре заявки по id



router = routers.DefaultRouter()
router.register(r'forms', FormSet, basename = 'анкеты') #анкеты
router.register(r'offers', OfferSet, basename = 'предложения') #предложения
router.register(r'bid', BidSet, basename = 'заявки') #заявки


urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^admin/dynamic_raw_id/', include('dynamic_raw_id.urls')),
]

#urlpatterns = 
#    path('admin/', admin.site.urls),
#]
