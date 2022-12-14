from model_utils.models import TimeStampedModel
from django.conf import settings
from django.db import models
from django.db.models import CheckConstraint, Q, UniqueConstraint
from django.contrib.auth.models import User
from eox_rates.edxapp_wrapper.course_module import get_course_overview


class EoxRates(models.Model):
    """
    Model to persist rating for a course.
    """
    rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(get_course_overview(), on_delete=models.CASCADE, related_name='course', null=True)
    comment = models.TextField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(rate__range=(0, 5)), name='valid_rate'),
            models.UniqueConstraint(fields=["user", "rate"], name="unique_course_user_rating")
        ]
