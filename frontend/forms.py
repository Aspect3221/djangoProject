from django import forms
from django.core.exceptions import ValidationError

from frontend.validators import validateCreditCard


class CreditCardForm(forms.Form):
    # credit_card_number = forms.CharField(validators=validateCreditCard)
    # credit_card_number = forms.CharField(label="Test", max_length=1)
    print('test')
