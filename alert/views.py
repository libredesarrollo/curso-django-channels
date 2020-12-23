from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token

from .models import Alert

@login_required
def index(request):
    alerts = Alert.objects.all()
    token, _ = Token.objects.get_or_create(user=request.user)

    return render(request,'alert/index.html',{'alerts': alerts,'token':'Token_'+str(token)})

