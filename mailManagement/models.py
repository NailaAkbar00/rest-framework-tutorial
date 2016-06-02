from django.db import models


class actor(models.Model):
    actor_id = models.SmallIntegerField()
    first_name= models.CharField(max_length=40, blank=True, default='')
    last_name = models.CharField(max_length=40, blank=True, default='')
    last_update = models.DateTimeField(auto_now_add = True)
    