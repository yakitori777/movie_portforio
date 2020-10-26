from django.shortcuts import render
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from movieapp.models import MovieDetailModel
from buyapp.models import ScheduleModel, TicketHistoryModel
from django.shortcuts import redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Sum

# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html' ,{'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '',password2)
            user.save()
            return redirect('login')
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html' ,{'error':'ユーザーが存在しないかパスワードが間違っています'})
    return render(request, 'login.html')

def indexfunc(request):
    movie_object_list = MovieDetailModel.objects.all()
    ranking_dict = TicketHistoryModel.objects.values('schedule_model__movie_detail_model').annotate(total_price=Sum('price')).order_by('-total_price')
    ranking_list = []
    count = 0
    for item in ranking_dict:
        ranking_list.append(MovieDetailModel.objects.get(pk=item['schedule_model__movie_detail_model']))
        if count >= 5:
            break
        count += 1
    return render(request, 'index.html', {'movie_object_list':movie_object_list, 'ranking_list':ranking_list})

class MemberUpdate(UpdateView):
    template_name = 'memberUpdate.html'
    model = Profile
    fields = ('name','address','tel','point')
    success_url = reverse_lazy('index')

class MemberDetail(DetailView):
    template_name = 'memberMypage.html'
    model = Profile

def member_movie_history_func(request,pk):
    movie_history = TicketHistoryModel.objects.filter(profile__pk=pk).order_by('schedule_model__show_date')
    return render(request, 'memberMovieHistory.html', {'movie_history_list':movie_history})


def logoutfunc(request):
    logout(request)
    return redirect('index')