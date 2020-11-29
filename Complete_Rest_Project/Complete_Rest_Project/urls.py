"""Complete_Rest_Project URL Configuration
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
from django.conf.urls import url,include
from app1.views import function,Carspace
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('carspace',Carspace,basename='carspace')


from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('function',function),
    #path('function/',views.function),
    path('first_app/',views.first_app),
    path('',include(router.urls)),
    path('params/',views.Params.as_view({'get':'list'})),
    path('get_one_car/<int:pk>',views.Params.as_view({'get':'retrieve'})),
    path('update_cars/<int:pk>',views.PostData.as_view({'put':'update'})),
    path('delete_cars/<int:pk>', views.PostData.as_view({'delete': 'destroy'})),
    path('tyres/',views.Tyres.as_view(),),
    path('get_one_tyre/<product>',views.Get_one_tyre.as_view()),
    path('update_tyres/<product>',views.Update_tyres.as_view()),




]