from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "shop"
urlpatterns = [
    path('', views.profile, name="profile"),
    path('products/', views.product_list, name='products'),
    path('products/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('products_filter/<str:ordering>/', views.product_list, name='products_by_filter'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name='register'),

]
