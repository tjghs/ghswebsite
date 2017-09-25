from ..hours.models import HourRequest


def unapproved_requests(request):
    return {
        'num_outstanding': HourRequest.objects.filter(approved=False, rejected=False).count()
    }
