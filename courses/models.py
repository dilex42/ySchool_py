from django.db import models
from django.core.exceptions import ValidationError


class Course(models.Model):
    title = models.CharField(unique=True, max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    lecture_count = models.IntegerField()

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("End date cannot be before start date!")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
