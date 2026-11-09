from django.db import models


class Inquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    course = models.CharField(max_length=120, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "inquiries"

    def __str__(self):
        return f"{self.name} — {self.email}"
