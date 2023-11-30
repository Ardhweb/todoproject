from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
 

class TodoList(models.Model):
    OPEN = "Open"
    WORKING = "Working"
    DONE = "Done"
    OVERDUE = "Overdue"

    STATUS_CHOICES = [
        (OPEN, "Open"),
        (WORKING, "Working"),
        (DONE, "Done"),
        (OVERDUE, "Overdue"),
    ]
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=100, blank=False)
    due_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=OPEN, blank=False)

    def __str__(self):
        return self.title
