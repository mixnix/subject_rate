from django.forms import ModelForm

from .models import Review


class CreateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['course_name', 'professor_name', 'how_easy', 'how_interesting', 'review_body']
