from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    names=["GIFONE.gif","GIFTWO.gif","GIFTHREE.gif","GIFFOUR.gif"]
    return render(request, "board/index.html", {"gif": random.choice(names)})