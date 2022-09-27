import nested_admin.nested
from django.contrib import admin

# Register your models here.
from django.db.models import Avg

from account.models import Score
from questions.models import Question, Answer, Test


class UserInLine(nested_admin.NestedStackedInline):
    model = Score
    readonly_fields = ['score', 'test', 'email']
    max_num = 0


class AnswerInLine(nested_admin.NestedStackedInline):
    model = Answer
    max_num = 1


class QuestionInLine(nested_admin.NestedStackedInline):
    model = Question
    inlines = [AnswerInLine]
    min_num = 1


class TestAdmin(nested_admin.NestedStackedInline):
    model = Test
    list_display = ['title', 'group', 'question']
    inlines = [QuestionInLine, UserInLine]

    def questions(self, obj: Test):
        return obj.questions.count()

    def passed(self, obj: Test):
        return obj.score.count()

    def leader(self, obj: Test):
        if obj.rating.filter(rating__gt=0):
            return obj.rating.all().order_by('rating').first().login
        return '-'

    def leader_score(self, obj: Test):
        if obj.score.all():
            return obj.score.all().order_by('-score').first().score
        return '-'

    def avg_score(self, obj: Test):
        if obj.score.all():
            return obj.score.aggregate(Avg('score'))['score__avg']
        return '-'


admin.site.register(Test)

