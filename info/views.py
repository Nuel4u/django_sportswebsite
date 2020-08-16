from django.shortcuts import render
from django.views.generic import View
# Create your views here.

#from django.conf import settings
#from django.contrib import messages
#from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView ,DetailView ,View 
#from .forms import checkoutForm ,CouponForm,RefundForm,PaymentForm
#from django.views.generic.detail import  DetailView
#from django.views.generic import  View
#from django.shortcuts import redirect
#from django.utils import timezone
#from .forms import CheckoutForm
# , CouponForm, RefundForm, PaymentForm
#from .models import Item, OrderItem ,Order,Address,Payment ,Coupon,Refund,UserProfile
#import random
#import string
#import stripe

#from django.shortcuts import render
#from .models import *
#from django.http import JsonResponse
#import json
#import datetime
#from .utility import *

#class HomeView(ListView):
 #   template_name  = 'home-page.html'

def home(request):
    return render(request ,'home.html')



def about(request):

    return render(request ,'about.html')


def mission(request):
    return render(request ,'mission.html')

def training(request):

    return render(request ,'training.html')

def registration(request):

    return render(request ,'registration.html')

def contact(request):

    return render(request ,'contact.html')    