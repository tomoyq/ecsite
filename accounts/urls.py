from django.urls import path

from .views import *

urlpatterns = [
    path('regist/', RegistView.as_view(), name='regist'),
    path('regist_done/', RegistDoneView.as_view(), name='registDone'),
]