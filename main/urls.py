from django.urls import path
from .views import *

urlpatterns = [
    path('course/', Course_List_View.as_view(), name="course_list"),
    path('course/<str:name>/', Chapter_List_View.as_view(), name="chapter_list"),
    path('course/<str:course>/<str:chapter>/', Summary_View.as_view(), name="summary"),
]