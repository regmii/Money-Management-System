from django.urls import path
from .views import *
from .import views


app_name = 'deposit'
urlpatterns = [
    path('deposit/all/', DepositListView.as_view(), name='deposit-list'),
    path('deposit/new/', NewDeposit.as_view(), name="new-deposit"),
    path('person/new', NewPersonCreate.as_view(), name="new-person"),
    path('institution/new', NewInsitutionCreate.as_view(), name="new-institution"),
    path('institution/type/new', InstitutionTypeCreate.as_view(), name="new-institution-type"),

    #ajax
    path('abc/', views.person_ajax, name='deposit-ajax')
]