from django.db import models
#study up on necessary models
class Stuffs(models.Model):
    content = models.TextField(blank = True, null = True)