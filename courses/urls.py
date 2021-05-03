from django.urls import path
from .views import CourseList, CourseDetail


urlpatterns = [
    path("courses/", CourseList.as_view(), name="course_list"),
    path("courses/<int:pk>/", CourseDetail.as_view(), name="course_detail"),
]
