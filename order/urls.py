from django.urls import path
from . import views

app_name = "order"
urlpatterns = [
    path('verify_phone/', views.verify_phone, name="verify_phone"),
    path('verify_code', views.verify_code, name="verify_code"),
    path('crate_order/', views.create_order, name="create_order"),
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
    path('order_list/', views.orders_list, name='order_list'),
    path('order_detail/<int:id>/', views.order_detail, name="order_detail")
]
