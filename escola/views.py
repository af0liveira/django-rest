from rest_framework import viewsets

from escola.models import Aluno
from escola.serializers import AlunoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
