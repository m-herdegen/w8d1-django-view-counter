from django.shortcuts import render
from django.http import HttpResponse
import datetime 
import random 

# Create your views here.

users = {}

def set_cookies(request):
    response = render(request, 'counter_app/count.html')
    response.set_cookie('hey', 'there', max_age=5)
    response.set_cookie('clementine', 'tangerine', httponly=True)

    return response

def increment_count(request):
    print(request.COOKIES)
    user_id = request.COOKIES.get('user_id')
    user = users.get(user_id)

    if not user:
        user_id = str(random.randint(100000,999999))

        users[user_id] = {
            'count': 1,
            'start_time': datetime.datetime.now()
        }
    else:
        users[user_id]['count'] += 1

    response = render(request, 'counter_app/index.html', users[user_id])
    response.set_cookie('user_id', user_id)
    return response