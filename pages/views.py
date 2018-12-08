from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator


from .models import Review, Professor, CourseName
from .forms import CreateReviewForm
from .decorators import user_is_review_post_user


class IndexView(TemplateView):
    template_name = 'pages/index.html'


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'pages/review_list.html'
    context_object_name = "review_list"
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


def ReviewCreateView(request):
# if this is a POST request we need to process the form data

    # user = request.user
    # employee = user.employee

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateReviewForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # check if course code is the same as in the used course name
            # if not then check if there is a course with such a course code plus course name
            # if not then create such a course
            # manually create a review and save it

            # then i want to create a field with data list
            # data list should be dynamically created after picking subject
            form.instance.author = request.user
            form.save()

            # # Save User model fields
            # user.first_name = request.POST['first_name']
            # user.last_name = request.POST['last_name']
            # user.save()
            #
            # # Save Employee model fields
            # employee.company = request.POST['company']
            # employee.news_notifications = request.POST['news_notifications']
            # employee.save()

            # redirect to the index page
            return HttpResponseRedirect(reverse('review-list'))

    # if a GET (or any other method)
    else:
        # form = UserSettingsForm(instance=user)

        # I am gonna populate it with unique course names
        # CourseName.objects.values('course_name').distinct()
        form = CreateReviewForm()

    return render(request, 'pages/review_new.html', {'form': form})


# class ReviewCreateView(LoginRequiredMixin, FormView):
#     model = Review
#     template_name = 'pages/review_new.html'
#     form_class = CreateReviewForm
#     success_url = reverse_lazy('review-list')
#
#     def form_valid(self, form):
#         # todo dlaczego tutaj przypisujesz jakiegos autora,
#         # wydaje mi sie ze powinienes tu sprawdzic czy wprowadzili
#         # poprawne wiadomosci by nie mozna bylo na sile wyslac zlych wartosci
#         # ktore zapisze serwer do bazy danych
#         # wyszukaj na stack overflow to
#         # popraw to tez w review update view
#         form.instance.author = self.request.user
#         form.save()
#         return super().form_valid(form)


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



