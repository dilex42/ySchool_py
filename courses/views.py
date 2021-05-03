from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from .serializers import CourseSerializer


class CourseList(generics.ListCreateAPIView):
    """
    get:
    Return courses list with filtering. You can also search by title.
    post:
    Create new course.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["title"]
    filterset_fields = {
        "start_date": ["gte", "lte", "exact"],
        "end_date": ["gte", "lte", "exact"],
    }


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the given course.
    put:
    Update the given course.
    patch:
    Partially update the given course.
    delete:
    Delete the given course.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
