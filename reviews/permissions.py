from rest_framework import permissions

from reviews.models import Review


class IsAdminOrIsOwnUser(permissions.BasePermission):
    def has_permission(self, request, view):

        review_id = view.kwargs.get("review_id", None)
        review = Review.objects.get(id=review_id)

        if review.id == request.user.id or request.user.is_superuser:
            return True

        return False
