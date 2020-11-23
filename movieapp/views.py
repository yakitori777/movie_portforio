from django.shortcuts import render
from django.views.generic import ListView
from .models import MovieDetailModel
from buyapp.models import ScheduleModel
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import redirect
import datetime
import json
from django.http import JsonResponse

def movie_list_func(request):
    movie_list = MovieDetailModel.objects.all()
    return render(request, 'movieList.html', {'movie_list':movie_list})

def movie_detail_func(request,pk):
    movie_object = MovieDetailModel.objects.get(pk=pk)
    object_pk = pk
    datelist = []
    hourlist = []
    nowdate = timezone.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
    for date_num in range(7):
        format_date = nowdate + datetime.timedelta(days=date_num)
        datelist.append(format_date)
    for hour_num in range(12,21,3):
        hourlist.append(hour_num)
    return render(request, 'movieDetail.html',{'movie_object':movie_object, 'datelist':datelist, 'hourlist':hourlist, 'object_pk':object_pk})

def select_seat_func(request):
    if request.user.is_authenticated:
        object_pk = request.POST['object_pk']
        movie_object = MovieDetailModel.objects.get(pk=object_pk)
        date = request.POST['date']
        hour = request.POST['hour']
        schedule = request.POST['schedule']
        hour_num = int(hour)
        tdate = datetime.datetime.strptime(date, '%Y年%m月%d日%H:%M')
        show_date = tdate.replace(hour=hour_num)
        schedule_date = datetime.date(show_date.year, show_date.month, show_date.day)
        seat_list_array = ScheduleModel.objects.filter(movie_detail_model=movie_object, show_date=show_date, screen_num=object_pk).values_list('seat_name', flat=True)
        count = 0
        seat_list = ''
        for name in seat_list_array:
            if count == 0:
                seat_list = name
                count += 1
            else:
                seat_list += ',' + name
        return render(request, 'selectSeat.html',{'movie_object':movie_object, 'date':date, 'hour':hour, 'object_pk':object_pk, 'seat_list':seat_list, 'schedule':schedule, 'schedule_date':schedule_date})
    else:
        return redirect('login_error')

def login_error_func(request):
    return render(request, 'loginError.html')

def readme_func(request):
    return render(request, 'readme.html')

def vue_movie_list_func(request):
    movie = MovieDetailModel.objects.all().values()
    movie_object_list = list(movie)
    return JsonResponse(movie_object_list, safe=False)