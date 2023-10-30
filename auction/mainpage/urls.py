from django.urls import path
from . import views

urlpatterns = [
    path("auction/",views.index,name="auction"),
    path("auction/<slug:slug>",views.bid,name="bid")
]
