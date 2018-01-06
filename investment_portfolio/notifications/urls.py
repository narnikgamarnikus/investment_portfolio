
from django.conf.urls import url
from .views import CommandReceiveView

urlpatterns = [
    url(r'^(?P<bot_token>.+)/$', CommandReceiveView.as_view(), name='bot_receiver'),
    url(r'^telegram_auth/$', views.telegram_auth, name='telegram_auth' ),
]