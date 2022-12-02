
"""Backend abstraction for Course Module."""
import logging

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview  # pylint: disable=import-error


LOG = logging.getLogger(__name__)


def course_overview_backend():
    """Return CourseOverview class."""
    return CourseOverview
