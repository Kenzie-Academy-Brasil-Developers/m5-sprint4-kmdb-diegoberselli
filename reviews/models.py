from django.db import models


class CategoryReview(models.TextChoices):
    MUST_WATCH = ("MW", "Must Watch")
    SHOULD_WATCH = ("SW", "Should Watch")
    AVOID_WATCH = ("AW", "Avoid Watch")
    NO_OPINION = ("NO", "No Opinion")


class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recommendation = models.CharField(
        max_length=50, choices=CategoryReview.choices, default=CategoryReview.NO_OPINION
    )

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )

    critic = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
