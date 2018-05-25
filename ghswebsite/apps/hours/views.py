from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import HourRequestForm, HourItemForm
from .models import HourRequest, HourItem
from ..user.decorators import superuser_required


@login_required
def request_hours(request):
    """Hour requests """
    if request.method == 'POST':
        try:
            request_form = HourRequestForm(request.POST)
            hour_request = request_form.save(commit=False)
            hour_request.user = request.user
            hour_request.approved = False
            hour_request.save()
        except:
            # TODO: handle errors
            pass
    request_form = HourRequestForm()

    approved = HourRequest.objects.filter(user=request.user, approved=True, rejected=False)
    outstanding = HourRequest.objects.filter(user=request.user, approved=False, rejected=False)
    rejected = HourRequest.objects.filter(user=request.user, rejected=True)

    total_hours = sum([r.count * r.item.hours for r in approved])
    context = {
        'request_form': request_form,
        'outstanding': outstanding,
        'approved': approved,
        'rejected': rejected,
        'approved_hours': total_hours
    }
    return render(request, 'hours/request.html', context)


@superuser_required
def add_hour_item(request):
    if request.method == 'POST':
        item_form = HourItemForm(request.POST)
        try:
            item_form.save()
        except:
            pass
    item_form = HourItemForm()
    items = HourItem.objects.all()
    context = {
        'form': item_form,
        'items': items
    }
    return render(request, 'hours/add_item.html', context)


@superuser_required
def edit_hour_item(request, item):
    item = get_object_or_404(HourItem, pk=item)
    if request.method == 'POST':
        item_form = HourItemForm(request.POST, instance=item)
        if item_form.is_valid():
            item_form.save()
            return redirect("add_hour_item")
    item_form = HourItemForm(instance=item)
    context = {
        'form': item_form,
        'item': item
    }
    return render(request, 'hours/edit_item.html', context)

@superuser_required
def delete_hour_item(request, item):
    item = get_object_or_404(HourItem, pk=item)
    item.delete()
    return redirect("add_hour_item")


@superuser_required
def approve_hours(request):
    """Approve hours """
    all_requests = [{
        'title': r.item.title,
        'user': r.user.full_name,
        'id': r.pk,
        'desc': r.description,
        'item_hours': str(r.item.hours),
        'count': r.count,
        'total': str(r.count * r.item.hours),
        'date': str(r.date)
    } for r in HourRequest.objects.filter(approved=False, rejected=False)]
    context = {
        'requests': all_requests
    }
    return render(request, 'hours/approve.html', context)


@superuser_required
def approve_api(request):
    if request.method == 'POST':
        try:
            pk = request.POST['pk']
            do_approve = request.POST['action'] == 'approve'
            hr = HourRequest.objects.get(pk=pk)
            if do_approve:
                hr.approved = True
            else:
                hr.rejected = True
            hr.save()
            all_requests = [{
                'title': r.item.title,
                'user': r.user.full_name,
                'id': r.pk,
                'desc': r.description,
                'item_hours': str(r.item.hours),
                'count': r.count,
                'total': str(r.count * r.item.hours),
                'date': str(r.date)
            } for r in HourRequest.objects.filter(approved=False, rejected=False)]
            return JsonResponse(all_requests, safe=False)
        except Exception as e:
            return JsonResponse({'error': 'Error: {}'.format(e)})
    else:
        return JsonResponse({'error': 'Invalid HTTP method'})
