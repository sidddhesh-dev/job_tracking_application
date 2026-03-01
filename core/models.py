from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Offer', 'Offer'),
    ]

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    date_applied = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.company} - {self.role}"
    

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profiles/')
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField(help_text="Comma separated skills")
    certificates = models.TextField(help_text="Certificates info")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name