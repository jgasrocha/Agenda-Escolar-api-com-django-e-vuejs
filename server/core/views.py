from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Professor, Admin, Disciplina, AgendaFixa, TrocaAgenda
from .serializers import ProfessorSerializer, AdminSerializer, DisciplinaSerializer, AgendaFixaSerializer, TrocaAgendaSerializer

# Professores
@api_view(['GET', 'POST'])
def professor_list_create(request):
    if request.method == 'GET':
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def professor_detail(request, pk):
    try:
        professor = Professor.objects.get(pk=pk)
    except Professor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Admins
# Admin List & Create
@api_view(['GET', 'POST'])
def admin_list_create(request):
    if request.method == 'GET':
        admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        professor_id = request.data.get('professor')  # Pega o ID do professor
        if professor_id is None:
            return Response({"professor": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        try:
            professor = Professor.objects.get(pk=professor_id)
        except Professor.DoesNotExist:
            return Response({"professor": ["Professor with this ID does not exist."]}, status=status.HTTP_404_NOT_FOUND)

        # Verifica se já existe um admin para o professor
        admin, created = Admin.objects.get_or_create(professor=professor)  
        if created:
            return Response({
                "id": admin.id,
                "professor_id": professor.id,
                "professor_nome": professor.nome
            }, status=status.HTTP_201_CREATED)

        return Response({"detail": "Admin already exists."}, status=status.HTTP_400_BAD_REQUEST)


# Admin Detail
@api_view(['DELETE'])
def admin_delete(request, pk):
    try:
        admin = Admin.objects.get(pk=pk)
    except Admin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Admins - Check if professor is an admin
@api_view(['GET'])
def is_professor_admin(request, professor_id):
    try:
        # Verifica se existe um admin para o professor
        admin = Admin.objects.get(professor_id=professor_id)
        return Response({"is_admin": True}, status=status.HTTP_200_OK)
    except Admin.DoesNotExist:
        return Response({"is_admin": False}, status=status.HTTP_200_OK)


# View para listar e criar disciplinas
@api_view(['GET', 'POST'])
def disciplina_list_create(request):
    if request.method == 'GET':
        disciplinas = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Criação de uma nova disciplina
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View para detalhar, atualizar ou excluir uma disciplina
@api_view(['GET', 'PUT', 'DELETE'])
def disciplina_detail(request, pk):
    try:
        disciplina = Disciplina.objects.get(pk=pk)
    except Disciplina.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Atualizar disciplina
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Deletar disciplina
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Agenda Fixa
@api_view(['GET', 'POST'])
def agenda_fixa_list_create(request):
    if request.method == 'GET':
        agendas_fixas = AgendaFixa.objects.all()
        serializer = AgendaFixaSerializer(agendas_fixas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AgendaFixaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def agenda_fixa_detail(request, pk):
    try:
        agenda_fixa = AgendaFixa.objects.get(pk=pk)
    except AgendaFixa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AgendaFixaSerializer(agenda_fixa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AgendaFixaSerializer(agenda_fixa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        agenda_fixa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Troca de Agenda
@api_view(['GET', 'POST'])
def troca_agenda_list_create(request):
    if request.method == 'GET':
        trocas = TrocaAgenda.objects.all()
        serializer = TrocaAgendaSerializer(trocas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrocaAgendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def troca_agenda_detail(request, pk):
    try:
        troca_agenda = TrocaAgenda.objects.get(pk=pk)
    except TrocaAgenda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrocaAgendaSerializer(troca_agenda)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TrocaAgendaSerializer(troca_agenda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        troca_agenda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
