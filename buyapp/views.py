from django.shortcuts import render
from django.views.generic import ListView
from movieapp.models import MovieDetailModel
from memberapp.models import Profile
from .models import ScheduleModel, TicketHistoryModel
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from datetime import timedelta
import datetime
import uuid

def test_schedule_add_func(request):
    ScheduleModel.objects.all().delete()
    movie_detail_models = MovieDetailModel.objects.all()
    nowdate = timezone.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
    screen_num = 0
    logging.debug('debug message')
    for movie_detail_model in movie_detail_models:
        for date_num in range(7):
            for hour_num in range(12, 21, 3):
                schedule_model = ScheduleModel()
                schedule_model.movie_detail_model =  movie_detail_model
                schedule_model.show_date = nowdate + datetime.timedelta(days=date_num) + datetime.timedelta(hours=hour_num)
                schedule_model.screen_num =  screen_num
                schedule_model.save()
        screen_num += 1    
    movie_list = MovieDetailModel.objects.all()
    return render(request, 'movieList.html', {'movie_list':movie_list})

def check_purchase_func(request):
    submit_token = set_submit_token(request)
    ticket_category = ['一般', '大学生', '高校生', '小中学生', '幼児(3歳以上)']
    ticket_price_list = ['1800', '1500', '1000', '1000', '600']
    ticket_list =[]
    ticket_num_list =[]
    seat_list = request.POST['seat_list1']
    seat_list_array = seat_list.split(',')
    object_pk = request.POST['object_pk']
    ticket_total_price = request.POST['ticket_total_price']
    schedule = request.POST['schedule']
    ticket1 = request.POST['ticket1']
    ticket2 = request.POST['ticket2']
    ticket3 = request.POST['ticket3']
    ticket4 = request.POST['ticket4']
    ticket5 = request.POST['ticket5']
    ticket_num_list.append(ticket1)
    ticket_num_list.append(ticket2)
    ticket_num_list.append(ticket3)
    ticket_num_list.append(ticket4)
    ticket_num_list.append(ticket5)
    ticket_str = ""
    price_list = []
    price_list_str = ""
    tikect_num = 0
    i = 0
    for item in ticket_num_list:
        if item == "0":
            i += 1 
        else:
            ticket_num = int(item)
            for j in range(ticket_num):
                ticket_str = ticket_category[i] + "     " + ticket_price_list[i] 
                ticket_list.append(ticket_str)
                price_list.append(ticket_price_list[i])
            i += 1
    count = 0
    for price in price_list:
        if count == 0:
            price_list_str = price
            count += 1
        else:
            price_list_str += ',' + price
    i=0
    for item in ticket_list:
        ticket_list[i] = item + "     " + seat_list_array[i]
        i += 1
    total_ticket_num = int(ticket1) +int(ticket2) +int(ticket3) +int(ticket4) +int(ticket5)
    movie_object = MovieDetailModel.objects.get(pk=object_pk)
    date = request.POST['date']
    hour = request.POST['hour']
    hour_num = int(hour)
    tdate = datetime.datetime.strptime(date, '%Y年%m月%d日%H:%M')
    show_date = tdate.replace(hour=hour_num)
    schedule_date = datetime.date(show_date.year, show_date.month, show_date.day)
    for seat_name in seat_list_array:
        ScheduleModel.objects.create(movie_detail_model=movie_object, show_date=show_date, screen_num=object_pk, seat_name=seat_name)
    return render(request, 'checkPurchase.html',
                    {'movie_object':movie_object, 
                    'date':date, 'hour':hour, 
                    'object_pk':object_pk, 
                    'seat_list':seat_list, 
                    'show_date':show_date, 
                    'schedule':schedule,
                    'ticket_total_price':ticket_total_price, 
                    'total_ticket_num':total_ticket_num, 
                    'ticket_list':ticket_list, 
                    'price_list_str':price_list_str,
                    'schedule_date':schedule_date,
                    "submit_token": submit_token,
                    }
                )

@login_required
def purchase_func(request):
    if not exists_submit_token(request):
        return render(request, 'purchaseError.html', {})
    else:
        login_user_id = request.user.id
        object_pk = request.POST['object_pk']
        price_list_str = request.POST['price_list']
        ticket_total_price = request.POST['ticket_total_price']
        schedule = request.POST['schedule']
        movie_object = MovieDetailModel.objects.get(pk=object_pk)
        user = Profile.objects.get(pk=login_user_id)
        date = request.POST['date']
        hour = request.POST['hour']
        hour_num = int(hour)
        seat_list = request.POST['seat_list']
        seat_list_array = seat_list.split(',')
        price_list = price_list_str.split(',')
        tdate = datetime.datetime.strptime(date, '%Y年%m月%d日%H:%M')
        show_date = tdate.replace(hour=hour_num)
        schedule_date = datetime.date(show_date.year, show_date.month, show_date.day)
        user_point = Profile.objects.values('point').get(pk=login_user_id)
        if user_point['point'] >= int(ticket_total_price):
            now_user_point = user_point['point'] - int(ticket_total_price)
            user.point = now_user_point
            user.save()
            tdate = datetime.datetime.strptime(date, '%Y年%m月%d日%H:%M')
            show_date = tdate.replace(hour=hour_num)
            i=0
            for seat_name in seat_list_array:
                last_schedule_object = ScheduleModel.objects.last()
                last_schedule_object_id = int(last_schedule_object.pk)
                schedule_object_id = int(last_schedule_object_id+1)
                ScheduleModel.objects.create(movie_detail_model=movie_object, show_date=show_date, screen_num=object_pk, seat_name=seat_name)
                schedule_object = ScheduleModel.objects.get(pk= schedule_object_id )
                TicketHistoryModel.objects.create(profile=user, schedule_model=schedule_object, price=price_list[i])
                i += 1
            return render(request, 'purchase.html',
                            {'movie_object':movie_object,
                            'show_date':show_date, 
                            'ticket_total_price':ticket_total_price, 
                            'login_user_id':login_user_id,
                            'schedule':schedule,
                            'schedule_date':schedule_date,
                            'user':user
                            }
                        )
        else:
            return redirect('purchase_error')

def purchase_error_func(request):
    return render(request, 'purchaseError.html')

def set_submit_token(request):
    submit_token = str(uuid.uuid4())
    request.session['submit_token'] = submit_token
    return submit_token

def exists_submit_token(request):
    token_in_request = request.POST.get('submit_token')
    token_in_session = request.session.pop('submit_token', '')

    if not token_in_request:
        return False
    if not token_in_session:
        return False

    return token_in_request == token_in_session