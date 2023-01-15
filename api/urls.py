from django.urls import path

from api.views import CouponEventView


urlpatterns = [
    path('', CouponEventView.as_view())
]
