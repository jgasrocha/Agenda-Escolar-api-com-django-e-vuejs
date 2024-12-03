from django.urls import path
from .views import (
    agenda_fixa_list_create,
    troca_agenda_list_create,
    troca_agenda_detail,
    professor_list_create,
    professor_detail,
    admin_list_create,
    disciplina_list_create,
    disciplina_detail,
    is_professor_admin,
    admin_delete,
)

urlpatterns = [
    path('agendas/', agenda_fixa_list_create, name='agenda-fixa-list-create'),
    path('trocas/', troca_agenda_list_create, name='trocaagenda-list-create'),
    path('trocas/<int:pk>/', troca_agenda_detail, name='trocaagenda-detail'),
    path('professores/', professor_list_create, name='professor-list-create'),
    path('professores/<int:pk>/', professor_detail, name='professor-detail'),
    path('admins/', admin_list_create, name='admin-list-create'),
    path('admins/<int:pk>/', admin_delete, name='admin-delete'),
    path('disciplinas/', disciplina_list_create, name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', disciplina_detail, name='disciplina-detail'),
    path('is_professor_admin/<int:professor_id>/', is_professor_admin, name='is-professor-admin'),
]
