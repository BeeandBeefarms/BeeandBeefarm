from django.shortcuts import render
from django.http import HttpResponse
#from application import models
# Create your views here.

def landing_page(request):
    return render (request,'html/page1.html')

# def log_in_page(request):
#     return render(request,'html/loginpage.html')
#
# def order_sts_page(request):
#     return render(request,'html/order_sts3.html')
#
# def buy_sell_page(request):
#     return render(request,'html/buy_sell_page.html')
#
# def order_sts_main_page(request):
#     return render(request,'html/order_status_main_page.html')
#
# def sign_up_page(request):
#     return render(request,'html/sign_up_page.html')
#
