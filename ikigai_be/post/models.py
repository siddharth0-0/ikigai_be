from datetime import datetime

from django.contrib.auth import authenticate, get_user_model
from django.db import models



class Mood(models.Model):
    mood_id = models.AutoField(primary_key=True)
    mood_type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.mood_type)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_text = models.TextField()
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    mood_id = models.ForeignKey(Mood, on_delete=models.CASCADE)
    last_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return str(self.post_id)
