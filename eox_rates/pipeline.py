from openedx_filters.learning.filters import (
    CertificateCreationRequested,
    CertificateRenderStarted,
    CohortChangeRequested,
    CourseAboutRenderStarted,
    CourseEnrollmentStarted,
    CourseUnenrollmentStarted,
    DashboardRenderStarted,
    StudentLoginRequested,
    StudentRegistrationRequested,
    CohortAssignmentRequested,
)
from openedx_filters import PipelineStep


class RenderCourseReview(PipelineStep):
    """
    Stop course about render raising RenderCustomResponse exception.
    Example usage:
    Add the following configurations to your configuration file:
        "OPEN_EDX_FILTERS_CONFIG": {
            "org.openedx.learning.course_about.render.started.v1": {
                "fail_silently": False,
                "pipeline": [
                    "openedx_filters_samples.samples.pipeline.RenderAlternativeCourseAbout"
                ]
            }
        }
    """

    def run_filter(self, context, template_name):  # pylint: disable=arguments-differ
        """
        Pipeline step that renders a custom template.
        When raising the exception, this filter uses a redirect_to field handled by
        the course about view that redirects to the URL indicated.
        """

        context["course_review"] = "This is a custom course review charged from a pipeline filter"
        raise CourseAboutRenderStarted.RenderInvalidCourseAbout(
            "You can't view this course.",
            course_about_template='/eox_rates/templates/course_about_review.html',
            template_context=context,
        )
