from django.db import models

class SpanishWord(models.Model):
  spa = models.CharField(max_length=50, unique=True)
  pronunciation = models.CharField(max_length=50, default="", blank=True)
  eng = models.CharField(max_length=50)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  # if I don't add this, admin page will say: Post object(1) instead of the title
  def __str__(self):
    return self.spa
