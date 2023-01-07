from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
# Create your views here.

def author(request):
    # user_data = CustomUser.objects.all()
    auth_data = CustomUser.objects.filter(public_visibility=1)
    print(auth_data)
    return render(request, 'users/authordeets.html', {'cust': auth_data})
