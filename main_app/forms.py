from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['date', 'rating', 'comment']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Write your review here',
                    'rows': 4
                }
            ),
        }

