from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    # path('accounts/', include("django.contrib.auth.urls")),
    path('login', login_view, name="login"),
    path('registration', regist, name="registration"),
    path('logout', logout_view, name='logout'),
    path('activate-user/<str:uidb64>/<str:token>/', activate_user, name='activate'),
    path('password_reset/', WebPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/', WebPasswordResetConfirmationView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', WebPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_complete/', WebPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('password_reset_confirmation/', WebPasswordResetConfirmationView.as_view(), name='password_reset_confirm'),
    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]