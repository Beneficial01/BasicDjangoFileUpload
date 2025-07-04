from django.db import models

class SampleFile(models.Model):
    sample_id = models.CharField(max_length=100)
    file = models.FileField(upload_to='sample_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sample_id}: {self.file.name}"