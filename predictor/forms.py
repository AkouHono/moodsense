from django import forms


class EmotionForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "How are you feeling today?",
                "rows": 5,
                "class": "form-control",
            }
        )
    )