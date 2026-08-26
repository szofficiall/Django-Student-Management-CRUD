from django import forms
from .models import StudentData


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentData
        # fields = "__all__"
        fields = ["name", "age", "email"]

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 18:
            raise forms.ValidationError("Age must be greater than 18")

        return age

    widgets = {
        "name": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter student name",
            }
        ),
        "age": forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter student age",
            }
        ),
        "email": forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter student email",
            }
        ),
    }
