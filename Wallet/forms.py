from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SignUpForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username','password1', 'password2',)

class TransferForm(forms.Form):
    to = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)

    def clean_amount(self):
        data = self.cleaned_data['amount']
        if data <= 0:
            raise ValidationError(_('Invalid amount - must be greater than 0'))
        return data

    def clean_to(self):
        data = self.cleaned_data['to']
        try:
            user = User.objects.get(username=data)
        except User.DoesNotExist:
            raise ValidationError(u'Username "%s" Does Not Exist.' % data)    
        return data

class GiftForm(forms.Form):
    to = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def clean_amount(self):
        data = self.cleaned_data['amount']
        if data <= 0:
            raise ValidationError(_('Invalid amount - must be greater than 0'))
        return data

    def clean_to(self):
        data = self.cleaned_data['to']
        try:
            user = User.objects.get(username=data)
        except User.DoesNotExist:
            raise ValidationError(u'Username "%s" Does Not Exist.' % data)    
        return data
