from django.db import models

# Create your models here.
from groups.models import Group

CORRECT_ANSWER_CHOICE = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

class Test(models.Model):
    title = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='test')
    image = models.ImageField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='question')
    question = models.TextField()
    image = models.ImageField(blank=True)
    score = models.IntegerField(default=100)
    timer = models.IntegerField(default=20)


    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    C = models.CharField(max_length=100)
    D = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100, choices=CORRECT_ANSWER_CHOICE, default='A')

    def __str__(self):
        return self.correct_answer


