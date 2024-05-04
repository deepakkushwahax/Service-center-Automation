from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('login/', login , name = 'login'),
    path('register/', register , name = 'register'),
    path('booking/<str:phone>/', booking, name = 'booking'),
    path('feedback/<int:id>', feedback, name = 'feedback'),
    path('feedbacks/', feedbacks, name = 'feedbacks'),
    path('companies/', companies , name = 'companies'),
    path('bookcompanies/<str:type_of_vehicle>/', bookcompanies , name = 'bookcompanies'),
    path('bookings/', bookings , name = 'bookings'),
    path('logout/', logout, name='logout'),
    path('adminlog/', adminlog, name='adminlog'),
    path('adminhome/', adminhome, name='adminhome'),
    path('forgetpassword/', forgetpassword, name="forgetpassword"),
]