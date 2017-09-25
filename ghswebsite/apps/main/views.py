from django.shortcuts import render

from ..announcements.models import Announcement


def index(request):
    announcements = Announcement.objects.all()
    return render(request, "index.html", {
        'announcements': announcements
    })
