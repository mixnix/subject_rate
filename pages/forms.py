from django.forms import ModelForm, Form
from django import forms
from .models import Review, Professor, CourseName

#
# class CreateReviewForm(ModelForm):
#     class Meta:
#         model = Review
#         fields = ['course_name', 'professor_name', 'how_easy', 'how_interesting', 'review_body']
# #


class CreateReviewForm(Form):
    course_name = forms.ModelChoiceField(queryset=CourseName.objects.all())
    professor_name = forms.ModelChoiceField(queryset=Professor.objects.all())
    # todo: make constrainsts so that user can enter only value from 0 to 100
    how_easy = forms.IntegerField()
    how_interesting = forms.IntegerField()
    review_body = forms.CharField(widget=forms.Textarea)