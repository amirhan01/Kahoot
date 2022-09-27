from rest_framework import serializers

from account.models import CustomUser
from questions.models import Test, Question, Answer


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['questions_count'] = instance.questions_count()
        representation['test_passed'] = instance.score_count()
        return representation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'second_name', 'phone_number', 'login']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['score'] = instance.score.get(login=instance, test=self.context.get('test')).score
        representation['rating'] = instance.rating.get(login=instance, test=self.context.get('test')).rating
        representation['test_passed'] = instance.score.count()
        return representation


class TestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instance):
        passed_users = instance.score.all().order_by('-score')
        users = []
        for user in passed_users:
            user = CustomUser.objects.get(login=user.login)
            serializer = UserSerializer(user, context={'test': instance})
            users.append(serializer.data)
        representation = super().to_representation(instance)
        representation['leaders'] = users
        return representation


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class ListQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['answer'] = AnswersSerializer(instance.answer.all(), many=True).data
        return representation


class RetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['answer'] = AnswersSerializer(instance.answer.all(), many=True).data
        return representation


