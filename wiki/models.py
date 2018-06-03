from django.db import models


# Create your models here.
class Participant(models.Model):
    email = models.EmailField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Suggestion(models.Model):
    name_of_component = models.CharField(max_length=255)
    original_text = models.TextField()
    altered_text = models.TextField()
    language = models.CharField(max_length=255)
    reason = models.TextField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
