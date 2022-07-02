"""covid_19_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path as url
from covid_prediction import views
from covid_prediction import Register
from covid_prediction import login
from covid_prediction import predict_covid


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.index, name="HomePage"),
    path('index/', views.index),
    url('counties/',views.CountriesData),
    path('searchdata',views.CountriesDataJSON),
    url('register/', Register.Register),
    url('registerinsert', Register.RegisterInsert),
    url('login/', login.LogIn),
    path('PredictCovid', login.CheckLogin),
    url('covidData',predict_covid.PredictCovid),
    url('PreCovid',predict_covid.preCovid),
    url('submitCovid',predict_covid.submitCovid),
    path('countrydata/',views.countryDatabase),

]
