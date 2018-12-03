from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class CourseName(models.Model):


    course_name = models.CharField(max_length=225)

    course_code = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.course_name


class Professor(models.Model):
    professor_name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.professor_name


class Review(models.Model):

    course_name = models.ForeignKey(
        CourseName,
        on_delete=models.CASCADE
    )

    professor_name = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE
    )

    how_easy = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
    )

    how_interesting = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
    )

    creation_date = models.DateTimeField(auto_now_add=True)

    review_body = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review_body[:50]

    def get_absolute_url(self):
        return reverse('review-detail', args=[str(self.id)])
