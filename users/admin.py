# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ReviewsUserCreationForm, ReviewsUserChangeForm
from .models import ReviewsUser


class ReviewUserAdmin(UserAdmin):
    add_form = ReviewsUserCreationForm
    form = ReviewsUserChangeForm
    list_display = ['email', 'username', 'created_reviews']
    model = ReviewsUser


admin.site.register(ReviewsUser, ReviewUserAdmin)
