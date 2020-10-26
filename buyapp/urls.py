from django.urls import path
from .views import movie_list_func, movie_detail_func, test_schedule_add_func, check_purchase_func, purchase_func, purchase_error_func
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', movie_list_func, name='movie_list'),
    path('scheduleAdd/',test_schedule_add_func, name='schedule_add'),
    path('checkPurchase/',check_purchase_func, name='check_purchase'),
    path('purchase/', purchase_func, name='purchase'),
    path('purchaseError/', purchase_error_func, name='purchase_error'),
]
