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