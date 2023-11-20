from django.db import models

class Stuffs(models.Model):
    content = models.TextField(blank = True, null = True)