from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from frontend.forms import CreditCardForm
from frontend.validators import validateCreditCard


def index(request):
    return render(request, "index.html")

def task1(request):
    if request.method == "GET":
        return render(request, "task1.html")
    elif request.method == "POST":
        credit_card_number = request.POST.get("credit_card_number")
        if validateCreditCard(credit_card_number):
            messages.success(request, "Inputted Credit Card is correct")
            return redirect("task1")
        else:
            messages.error(request, "Wrong")
            return  redirect("task1")
