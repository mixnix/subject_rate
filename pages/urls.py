# pages/urls.py
from django.urls import path

from . import views
from .models import Professor, CourseName

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('all/', views.ReviewListView.as_view(), name='review-list'),

    path('<int:pk>/edit/',
         views.ReviewUpdateView.as_view(), name='review-edit'),
    path('<int:pk>/',
         views.ReviewDetailView.as_view(), name='review-detail'),
    path('<int:pk>/delete/',
         views.ReviewDeleteView.as_view(), name='review-delete'),
    path('new/', views.ReviewCreateView.as_view(), name='review-new'),
    path('new-professor/', views.ProfessorCreateView.as_view(model=Professor,
                                                             success_url='/reviews/'), name='professor-new'),
    path('new-course/', views.CourseCreateView.as_view(model=CourseName,
                                                       success_url='/reviews/'), name='course-new'),
    path('by-subject/', views.CourseBySubjectView.as_view(), name='reviews-by-subject'),

]
