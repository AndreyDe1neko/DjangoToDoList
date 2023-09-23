from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('auth', auth, name="login"),
    path('reg', regist, name="reg"),
    path('logout', logout_view, name='logout'),
    path('activate-user/<str:uidb64>/<str:token>/', activate_user, name='activate'),
    path('password_reset/', WebPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', WebPasswordResetDoneView.as_view(), name='password_reset_done' ),
    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]