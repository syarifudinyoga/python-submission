from django.db import models


class Question(models.Model):
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
    )
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    username = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
