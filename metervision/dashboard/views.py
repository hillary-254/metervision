from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dash(request):
    is_superuser = request.user.is_superuser
    return render(request, 'dashboard/index.html', {'is_superuser': is_superuser})
