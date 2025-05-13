from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.Charfield(max_length=200)
    content = models.DateTimeField(auto_now_add=True)

    def_str_(self):
    return self.title
