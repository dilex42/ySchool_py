from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "start_date", "end_date", "lecture_count"]

    def validate(self, attrs):
        if self.partial:
            if "start_date" not in attrs:
                attrs["start_date"] = self.instance.start_date
            if "end_date" not in attrs:
                attrs["end_date"] = self.instance.end_date
        instance = Course(**attrs)
        instance.clean()
        return attrs
