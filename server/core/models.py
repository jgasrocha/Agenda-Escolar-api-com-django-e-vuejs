from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True)
    senha = models.CharField(max_length=128, null=True)
    foto = models.ImageField(upload_to='fotos_professores/', blank=True, null=True)

    def __str__(self):
        return self.nome

    @property
    def is_admin(self):
        return Admin.objects.filter(professor=self).exists()

class Admin(models.Model):
    professor = models.OneToOneField(Professor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Admin: {self.professor.nome if self.professor else "Sem Professor"}'

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="disciplinas")

    def __str__(self):
        return self.nome

class AgendaFixa(models.Model):
    dia_semana = models.CharField(max_length=10, choices=[
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
    ])
    horario = models.TimeField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    local_foto = models.ImageField(upload_to='fotos_locais/', blank=True, null=True)
    descricao_local = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('dia_semana', 'horario') 

    def __str__(self):
        return f"{self.dia_semana.capitalize()} - {self.horario} - {self.disciplina.nome}"

class TrocaAgenda(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    agenda_fixa_original = models.ForeignKey(AgendaFixa, on_delete=models.CASCADE, related_name='agenda_original')
    horario_novo = models.TimeField()
    dia_novo = models.CharField(max_length=10, choices=[
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
    ])
    justificativa = models.TextField()
    aprovada = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Troca solicitada por {self.professor.nome} - {self.agenda_fixa_original} para {self.dia_novo} às {self.horario_novo}"