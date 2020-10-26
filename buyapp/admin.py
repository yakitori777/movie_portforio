from django.contrib import admin
from .models import TicketHistoryModel, ScheduleModel
# Register your models here.

admin.site.register(TicketHistoryModel)
admin.site.register(ScheduleModel)