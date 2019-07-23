from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE, related_name='profiles')
    user_profile = models.CharField(max_length=20, default=True)

    def __str__(self):
        return self.user_profile






