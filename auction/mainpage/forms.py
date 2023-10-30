from django import forms
from .models import Items,Bids

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["bid"]
        labels = {
            "bid": "Your Bid",
        }
