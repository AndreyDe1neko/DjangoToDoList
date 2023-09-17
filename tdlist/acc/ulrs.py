from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('auth', auth, name="auth"),
    path('reg', regist, name="reg"),
    path('logout', logout_view, name='logout'),
    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]