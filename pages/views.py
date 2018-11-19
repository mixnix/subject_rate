from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'pages/index.html'


# class ReviewListView(LoginRequiredMixin, ListView):


