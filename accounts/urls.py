from django.urls import path
from . import views

urlpatterns= [
    path('', views.home),
    path('admin-register/', views.admin_register, name='admin_register'),
    #path('user-register/<uuid:security_code>/', views.user_register, name='user_register'),
    path('secure/<str:security_code>/',views.user_register, name='user_register'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('barcode/<int:registration_id>/', views.generate_barcode, name='generate_barcode'),
    path('used-url/', views. used_url),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('home/', views.student_roombooking_page, name='home'),

]