from django.shortcuts import render, HttpResponse
from .models import Powerball

# Create your views here.


# def index(request):
#     latest_powerball = Powerball.objects.order_by('-date_drawing')[:5]
#     output = ', '.join([str(q.ball_1) for q in latest_powerball])
#     return HttpResponse(output)

def index(request):
    return render(request, 'index.html', {
        'date': date
    } )
