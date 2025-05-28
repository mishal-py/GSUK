
from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ["approved", "approved_by", "approval_date"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address_uk': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'address_nepal': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'membership_type': forms.Select(attrs={'class': 'form-select'}),
            'opt_out_contact': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rules_confirmed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class RejectionForm(forms.Form):
    reason = forms.CharField(
        label="Rejection Reason",
        widget=forms.Textarea(attrs={
            'class': 'form-control shadow-sm border-danger',
            'rows': 5,
            'placeholder': 'Explain the reason for rejection clearly...',
            'style': 'resize: none;',
        })
    )
