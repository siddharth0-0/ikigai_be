from django.db import models


class Privacy(models.Model):
    privacy_id = models.AutoField(primary_key = True)
    privacy_status = models.CharField(max_length= 30, blank=True)

    def __str__(self):
        return str(self.privacy_id)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    privacy_id = models.ForeignKey(Privacy, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)



