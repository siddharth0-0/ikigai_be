# from django.db import models
# from datetime import datetime
# from user.models import User


# class Mood(models.Model):
#     mood_id = models.AutoField(primary_key=True)
#     mood_type = models.CharField(max_length=50, blank=True)

#     def __str__(self):
#         return str(self.mood_id)


# class Post(models.Model):
#     post_id = models.AutoField(primary_key=True)
#     post_text = models.TextField(blank=True)
#     user_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
#     mood_id = models.ForeignKey(Mood, default=None, on_delete=models.CASCADE)
#     last_modified_by = models.IntegerField()
#     last_modified_date = models.DateField(default=datetime.now)

#     def __str__(self):
#         return str(self.post_id)
