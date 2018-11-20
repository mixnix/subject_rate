from django.core.exceptions import PermissionDenied
from .models import Review


def user_is_review_post_user(function):
    def wrap(request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs['pk'])
        if review.author_id == request.user.id:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    # wrap.__name__ = function.__name__
    return wrap
