from django.db import models


class EmotionAnalysis(models.Model):
    text = models.TextField()
    emotion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emotion} - {self.created_at}"