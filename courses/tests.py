from django.core.validators import ValidationError
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Course
from .serializers import CourseSerializer


class CourseModelTestCase(TestCase):
    def setUp(self):
        Course.objects.create(
            title="Literature",
            start_date="2021-04-20",
            end_date="2021-04-20",
            lecture_count=10,
        )
        Course.objects.create(
            title="History",
            start_date="2021-04-20",
            end_date="2021-04-20",
            lecture_count=12,
        )

    def test_lecture_count(self):
        course_lit = Course.objects.get(title="Literature")
        course_hist = Course.objects.get(title="History")
        self.assertEqual(course_lit.lecture_count, 10)
        self.assertEqual(course_hist.lecture_count, 12)

    def test_course_end_date_cannot_be_before_start_date(self):
        course = Course(
            title="Math",
            start_date="2021-02-01",
            end_date="2021-01-01",
            lecture_count=1,
        )
        with self.assertRaises(ValidationError):
            course.save()


class CourseListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("course_list")
        Course.objects.create(
            title="Literature",
            start_date="2021-04-20",
            end_date="2021-04-20",
            lecture_count=10,
        )
        Course.objects.create(
            title="History",
            start_date="2021-04-20",
            end_date="2021-04-20",
            lecture_count=12,
        )

    def test_create_course(self):
        response = self.client.post(
            self.url,
            {
                "title": "New Course",
                "start_date": "2021-04-20",
                "end_date": "2021-04-20",
                "lecture_count": 10,
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_create_course_duplicate(self):
        response = self.client.post(
            self.url,
            {
                "title": "Literature",
                "start_date": "2021-04-20",
                "end_date": "2021-04-20",
                "lecture_count": 10,
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["title"][0],
            "course with this title already exists.",
        )

    def test_retrieve_course_list(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.json()), Course.objects.count())

    def test_course_date_filter(self):
        Course.objects.create(
            title="New Course",
            start_date="2021-04-22",
            end_date="2021-04-23",
            lecture_count=12,
        )
        response = self.client.get(self.url, {"start_date__gte": "2021-04-21"})
        self.assertEqual(len(response.json()), 1)


class CourseDetailAPIViewTestCase(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Literature",
            start_date="2021-04-20",
            end_date="2021-04-20",
            lecture_count=10,
        )
        self.url = reverse("course_detail", kwargs={"pk": self.course.id})

    def test_course_object_retrieve(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        course_serializer_data = CourseSerializer(instance=self.course).data
        response_data = response.json()
        self.assertEqual(response_data, course_serializer_data)

    def test_course_object_update(self):
        response = self.client.put(
            self.url,
            {
                "title": "Science",
                "start_date": "2021-05-01",
                "end_date": "2021-05-01",
                "lecture_count": 18,
            },
        )
        response_data = response.json()
        course = Course.objects.get(id=self.course.id)
        self.assertEqual(response_data.get("title"), course.title)

    def test_course_object_partial_update(self):
        response = self.client.patch(self.url, {"lecture_count": 11})
        response_data = response.json()
        course = Course.objects.get(id=self.course.id)
        self.assertEqual(
            response_data.get("lecture_count"), course.lecture_count
        )

    def test_course_object_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
