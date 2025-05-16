from django.db import models
from django.contrib.auth.models import User

class CGPARecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_cgpa = models.FloatField()
    target_cgpa = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - CGPA: {self.current_cgpa} ➜ {self.target_cgpa}"


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=[('Beginner','Beginner'),('Intermediate','Intermediate'),('Advanced','Advanced')])
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class OutfitTip(models.Model):
    body_type = models.CharField(max_length=100)
    budget = models.CharField(max_length=50)
    tips = models.TextField()

    def __str__(self):
        return f"{self.body_type} - {self.budget}"
    

class MarathonEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    distance_km = models.FloatField()
    time_minutes = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.distance_km}km in {self.time_minutes}min"

class GymFriend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gym_user')
    location = models.CharField(max_length=100)
    preferred_time = models.CharField(max_length=50)
    matched_with = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='matched_friend')

    def __str__(self):
        return f"{self.user.username} - {self.location}"

class MovieSuggestion(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class MoodCheck(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy'),
        ('Sad', 'Sad'),
        ('Anxious', 'Anxious'),
        ('Motivated', 'Motivated'),
        ('Stressed', 'Stressed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    note = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood} ({self.date})"

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('Internship', 'Internship'),
        ('Part-time', 'Part-time'),
        ('Full-time', 'Full-time'),
        ('Remote', 'Remote'),
        ('Freelance', 'Freelance'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    apply_link = models.URLField()
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
    
class StudyGroup(models.Model):
    topic = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(User, related_name='joined_groups', blank=True)

    def __str__(self):
        return f"{self.topic} on {self.scheduled_date}"
