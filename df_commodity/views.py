from django.shortcuts import render,redirect
from django.db.models import Q
import hashlib
from models import *


def index(request):
    return  render(request,'df_commodity/index.html')
