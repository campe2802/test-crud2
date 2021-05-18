from django.db import models


# Create your models here.
class Tarea(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text