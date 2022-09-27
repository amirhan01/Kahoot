from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from questions.models import Test, Question
from questions.serializers import ListSerializer, TestUserSerializer, ListQuestionSerializer


class ListTestView(ListAPIView):
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Test.objects.filter(group=request.user.group)
        serializer = ListSerializer(queryset, context={'request': request}, many=True)

        if not serializer.data:
            return Response('Not found tests', status=400)

        return Response(serializer.data, status=200)


class TestUsersView(ListAPIView):
    serializer_class = TestUserSerializer
    permission_classes = []

    def list(self, request, test, *args, **kwargs):
        queryset = Test.objects.filter(title=test)
        serializer = TestUserSerializer(queryset, many=True)

        if not serializer.data:
            return Response('Не найдено!', status=400)

        return Response(serializer.data, status=200)


class ListQuestionsView(RetrieveAPIView):
    serializer_class = ListQuestionSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, test, *args, **kwargs):
        queryset = Question.objects.filter(test=test)
        serializer = ListQuestionSerializer(queryset, many=True)

        if not serializer.data:
            return Response(f'Not found this test {test}', status=404)

        return Response(serializer.data, status=200)







