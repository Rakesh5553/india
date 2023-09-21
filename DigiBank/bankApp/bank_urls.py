from django.contrib import admin
from django.urls import path
import bankApp.views  as bv
urlpatterns = [
    path('home', bv.home),
    path('bank_board/', bv.board),
    path('new-account/', bv.openAccount),
    path('acc_record/',bv.newAccountRecord),
    path('acc_record/<int:accNo>',bv.newAccountRecord),
    path('login/',bv.custLogin),
    path('branches/',bv.branches),
    path('loan/',bv.loan),
    path('invest/',bv.invest),
    
]