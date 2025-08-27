from django import forms
from .models import Approach

# -----------------------
# Approach Form (ModelForm)
# -----------------------
class ApproachForm(forms.ModelForm):
    class Meta:
        model = Approach
        fields = ["name", "email", "message"]  # match your model fields
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Your Message"}),
        }

# -----------------------
# Contact Form
# -----------------------
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Name', "class": "form-control"})
    )
    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile No', "class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'E-Mail', "class": "form-control"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': 4, "class": "form-control"})
    )

# -----------------------
# Payment Form
# -----------------------
PAYMENT_CHOICES = [
    ("card", "Debit/ Credit Card"),
    ("gpay", "Google Pay"),
    ("phonepe", "Phone Pay"),
    ("paytm", "Paytm"),
    ("amazon", "Amazon Pay"),
    ("whatsapp", "WhatsApp"),
]

class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
