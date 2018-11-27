from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


from .models import Review, Professor, CourseName
from .forms import CreateReviewForm
from .decorators import user_is_review_post_user


class IndexView(TemplateView):
    template_name = 'pages/index.html'


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'pages/review_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)

        subject_list = []
        for review in Review.objects.all():
            subject_list.append(review.course_name.course_name)
        context['subject_list'] = subject_list
        return context


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = 'pages/review_detail.html'


@method_decorator(user_is_review_post_user, name='dispatch')
class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = 'pages/review_new.html'
    form_class = CreateReviewForm


@method_decorator(user_is_review_post_user, name='dispatch')
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'pages/review_delete.html'
    success_url = reverse_lazy('review-list')


class ReviewCreateView(LoginRequiredMixin, FormView):
    model = Review
    template_name = 'pages/review_new.html'
    form_class = CreateReviewForm
    success_url = reverse_lazy('review-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class ProfessorCreateView(LoginRequiredMixin, CreateView):
    model = Professor
    template_name = 'pages/professor_new.html'
    fields = ['professor_name']
    login_url = 'login'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = CourseName
    template_name = 'pages/course_new.html'
    fields = ['course_name']
    login_url = 'login'


class CourseBySubjectView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'pages/review_list_by_subject.html'
    login_url = 'login'
    paginate_by = 10

    def get_queryset(self):
        return Review.objects\
            .filter(course_name__course_name__icontains=self
                    .request.GET.get('myquery', ''))\
            .order_by('creation_date')



