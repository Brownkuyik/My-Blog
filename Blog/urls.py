
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', Signup, name='signup'),
    path('login/', LOGIN.as_view(), name='login'),
    path('', home, name='Home'),
    path('Post_Details/<int:pk>/', Post_Detail, name='Post_Detail'),
    path('search_result/', Search_Result, name='Search_Result'),
    path('Category/<str:category>/', Category, name='category'),
]