from django.urls import path
from . import views
urlpatterns = [
    path('<int:month>', views.int_month),
    path('<str:month>', views.month, name = 'month_challenge'),
    path('', views.index, name = 'index')
    ]