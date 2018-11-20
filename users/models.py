from django.contrib.auth.models import AbstractUser
from django.db import models


class ReviewsUser(AbstractUser):
    created_reviews = models.PositiveIntegerField(default=0)