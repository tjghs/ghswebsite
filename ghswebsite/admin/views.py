from django.shortcuts import render


def admin_index(request):
    return render(request, 'admin_index.html')
