from django import forms

from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ("name", "email", "course", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "autocomplete": "email"}),
            "course": forms.Select(
                attrs={"placeholder": "Choose a course"},
                choices=[
                    ("", "Choose a course (optional)"),
                    ("Data Science Foundations", "Data Science Foundations"),
                    ("Machine Learning in Practice", "Machine Learning in Practice"),
                    ("Generative AI & LLMs", "Generative AI & LLMs"),
                    ("Python for Data Analysis", "Python for Data Analysis"),
                ],
            ),
            "message": forms.Textarea(
                attrs={"placeholder": "Tell us what you would like to learn...", "rows": 4}
            ),
        }
