from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from frontend.functions import validateCreditCard, calculateError, passwordCracker, encrypt, decrypt


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
            return redirect("task1")


def task2(request):
    if request.method == "GET":
        print('hi')
        return render(request, "task2.html")
    elif request.method == "POST":
        bitInput = request.POST.get("bitInput")
        if bitInput is not None:
            hammingCode = calculateError(bitInput)
            return render(request, "task2.html", {'hammingCode': hammingCode})


def task3(request):
    if request.method == "GET":
        return render(request, "task3.html")
    elif request.method == "POST":
        password = request.POST.get("password")
        if password is not None:
            passwordHash, result, attackType = passwordCracker(password)
            return render(request, "task3.html", {'hash': passwordHash, 'result': result, 'attackType': attackType})


def task4(request):
    if request.method == "GET":
        return render(request, "task4.html")
    elif request.method == "POST":
        plainMessage = request.POST.get("plain_message")
        toEncrypt = request.POST.get("to_encrypt")

        encryptedInput, key, cipherText = encrypt(plainMessage, toEncrypt)
        decryptedMessage = decrypt(encryptedInput, key)

        return render(request, "task4.html",
                      {'key': key, 'encryptedMessage': encryptedInput, 'decryptedMessage': decryptedMessage,
                       'cipherText': cipherText})
