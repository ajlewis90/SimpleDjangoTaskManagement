"""
A single Task model. There is no owner field on purpose, this version
of the app has no login, so every task just sits in one shared list
that anyone visiting the site can see and manage.
"""
from django.db import models
from django.urls import reverse


class Task(models.Model):

    class Status(models.TextChoices):
        TODO = 'todo', 'To do'
        IN_PROGRESS = 'in_progress', 'In progress'
        DONE = 'done', 'Done'

    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Newest tasks first by default, feels more natural for a
        # simple to-do style list than sorting by id.
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks:task_detail', kwargs={'pk': self.pk})

    @property
    def is_overdue(self):
        # Used in the templates to flag tasks that are late and not
        # yet marked done, kept as a property so the logic lives in
        # one place instead of being repeated in every template.
        from django.utils import timezone
        if not self.due_date or self.status == self.Status.DONE:
            return False
        return self.due_date < timezone.localdate()
