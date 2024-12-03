from rest_framework import serializers
from .models import Professor, Admin, Disciplina, AgendaFixa, TrocaAgenda

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
    professor_nome = serializers.CharField(source='professor.nome', read_only=True)  # Campo apenas para leitura
    professor_id = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all(), source='professor')

    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'professor_nome', 'professor_id']

class AgendaFixaSerializer(serializers.ModelSerializer):
    disciplina = DisciplinaSerializer(read_only=True)

    class Meta:
        model = AgendaFixa
        fields = '__all__'

class TrocaAgendaSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer(read_only=True)
    agenda_original = AgendaFixaSerializer(read_only=True)

    class Meta:
        model = TrocaAgenda
        fields = '__all__'
