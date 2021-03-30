from django import forms
from .models import *

class DepositCreateForm(forms.ModelForm):
    class Meta:
        model = Deposits
        fields = ['account_no', 'amount', 'by', 'deposit_method', 'institution', 'branch', 'purpose', 
                    'business_name', 'source', 'cheque_no', 
        ]
        widgets = {
            'amount':forms.NumberInput(attrs={
                'class':'form-control',
            }),

            'by':forms.Select(attrs={
                'class':'form-control',
            }),

            'account_no':forms.TextInput(attrs={
                'class':'form-control',
            }),

            'deposit_method':forms.Select(attrs={
                'class':'form-control',
            }),

            'institution':forms.Select(attrs={
                'class':'form-control',
            }),

            'branch':forms.TextInput(attrs={
                'class':'form-control',
            }),

            'purpose':forms.Select(attrs={
                'class':'form-control',
            }),

            'business_name':forms.TextInput(attrs={
                'class':'form-control',
            }),

            'source':forms.TextInput(attrs={
                'class':'form-control',
            }),

            'cheque_no':forms.TextInput(attrs={
                'class':'form-control',
            }),

            'cheque_image':forms.FileInput(attrs={
                'class':'form-control',
                'title':'upload image'
            }),

            'deposit_slip_image':forms.FileInput(attrs={
                'class':'form-control',
                'title':'upload image'
            }),

        }

class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = PersonDetail
        fields = ['name', 'contact', 'address']

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
            }),

            'contact':forms.TextInput(attrs={
                'class':'form-control',
            }),

            'address':forms.TextInput(attrs={
                'class':'form-control',
            }),

        }