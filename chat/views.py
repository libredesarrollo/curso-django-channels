from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required
def room(request, room_id):

    print("_______")
    print(request.GET['name'])

    try:
        room = request.user.rooms_joined.get(id=room_id)
    except:
        return HttpResponseForbidden()

    return render(request, 'chat/room.html', {'room':room})

# Create your views here.
