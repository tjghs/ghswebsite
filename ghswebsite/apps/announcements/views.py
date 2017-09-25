from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import AnnouncementForm
from ..user.decorators import superuser_required


@superuser_required
def create_announcement_view(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = AnnouncementForm()
    return render(request, 'announcements/new.html', {'form': form})
