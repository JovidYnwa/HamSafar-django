from django.shortcuts import render
from django.contrib.auth.models import User

def main_view(request):
    return render(request, 'trip/index.html', {})

def profile_view(request):
    greetting = 'Hey!'
    user = request.user
    full_name = user.get_full_name()
    query = User.objects.get(pk = user.pk)
    context = {
        'user':query,
        'greet':greetting,
        'full_name': user.get_full_name()
    }
    return render(request, 'account/profile.html', context)