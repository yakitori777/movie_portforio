from django.db import models
from memberapp.models import Profile
from movieapp.models import MovieDetailModel
import datetime

# Create your models here.
class ScheduleModel(models.Model):
    #映画情報
    movie_detail_model = models.ForeignKey(MovieDetailModel ,on_delete=models.PROTECT)
    #上映日時
    show_date = models.DateTimeField()
    #スクリーン番号
    screen_num = models.IntegerField()
    #座席名
    seat_name = models.CharField(max_length=10)

class TicketHistoryModel(models.Model):
    #会員情報
    profile = models.ForeignKey(Profile,on_delete=models.PROTECT)
    #映画スケジュール
    schedule_model = models.ForeignKey(ScheduleModel ,on_delete=models.PROTECT)
    #購入金額
    price = models.IntegerField()
    
