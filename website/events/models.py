from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1500)
    post_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    source = models.ForeignKey("Resource", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='events_images/', default='events_images/default.jpg')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.event.title} ({self.id})"


class Resource(models.Model):
    name = models.CharField(max_length=64, null=False)
    link = models.URLField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='subscribers')

    class Meta:
        unique_together = ('user', 'resource')

    def __str__(self):
        return f"{self.user.username} -> {self.resource.name}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_likes')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} likes {self.event.title}"
