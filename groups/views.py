from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from groups.models import Group
from groups.serializers import GroupSerializer


class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


