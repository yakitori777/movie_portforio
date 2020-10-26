from django.urls import path
from .views import signupfunc, loginfunc, indexfunc, MemberUpdate, logoutfunc, MemberDetail, member_movie_history_func

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('update/<int:pk>', MemberUpdate.as_view(), name='member_update'),
    path('mypage/<int:pk>', MemberDetail.as_view(), name='member_mypage'),
    path('history/<int:pk>', member_movie_history_func, name='member_history'),
    path('', indexfunc, name='index'),
]
