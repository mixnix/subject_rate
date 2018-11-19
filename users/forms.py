# users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ReviewsUser


class ReviewsUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = ReviewsUser
        fields = ('username', 'email')


class ReviewsUserChangeForm(UserChangeForm):

    class Meta:
        model = ReviewsUser
        fields = ('username', 'email')
