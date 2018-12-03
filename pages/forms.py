from django.forms import ModelForm, Form, widgets
from django import forms
from .models import Review, Professor, CourseName


class CreateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['course_name', 'professor_name', 'how_easy',
                  'how_interesting', 'review_body']

    # todo: w htmlu te inputy nie maja labeli przez co chyba nie sa powiazane
    course_name = forms.ModelChoiceField(queryset=CourseName.objects.all(),
                                         widget=forms.Select(attrs={'style': 'width:100%'}))
    professor_name = forms.ModelChoiceField(queryset=Professor.objects.all(),
                                            widget=forms.Select(attrs={'style': 'width:100%'}))
    course_code = forms.CharField(widget=forms.TextInput(attrs={'style': 'width:100%'}))

    how_easy = forms.IntegerField(
        widget=widgets.NumberInput(attrs={
            'id': 'easyslider', 'type': 'range', 'step': '1',
            'onchange': 'setval(this, easyval)',
            'oninput': 'setval(this, easyval)',
            'style': 'width:100%',
        }))
    how_interesting = forms.IntegerField(
        widget=widgets.NumberInput(attrs={
            'id': 'interestslider', 'type': 'range', 'step': '1',
            'onchange': 'setval(this, interestval)',
            'oninput': 'setval(this, interestval)',
            'style': 'width:100%',
        }))
    review_body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'width:100%'}))

