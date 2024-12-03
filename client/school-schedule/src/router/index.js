import { createRouter, createWebHistory } from 'vue-router';
import AdminFormPage from '../pages/Admin/AdminFormPage.vue';
import ProfessorFormPage from '../pages/Professor/ProfessorFormPage.vue';
import ProfessorListaPage from '../pages/Professor/ProfessorListaPage.vue';
import ProfessorEdit from '../components/Professor/ProfessorEdit.vue';
import AdminListPage from '../pages/Admin/AdminListPage.vue';
import AgendaPage from '../pages/Agenda/AgendaPage.vue';
import DisciplinaList from '../pages/Disciplinas/DisciplinaListPage.vue';
import DisciplinaForm from '../pages/Disciplinas/DisciplinaFormPage.vue';
import DisciplinaEdit from '../pages/Disciplinas/DisciplinaEditPage.vue';

const routes = [
  {
    path: '/criar-admin',
    name: 'CriarAdmin',
    component: AdminFormPage,
  },
  {
    path: '/criar-professor',
    name: 'CreateProfessor',
    component: ProfessorFormPage,
  },
  {
    path: '/professores',
    name: 'professoresPage',
    component: ProfessorListaPage,
  },
  {
    path: '/professores/editar/:id',
    name: 'editarProfessor',
    component: ProfessorEdit,
    props: true, // Certifique-se de que este componente existe
  },
  {
    path: '/admins',
    name: 'adminList',
    component: AdminListPage,
  },
  {
    path: '/agenda',
    name: 'Agenda',
    component: AgendaPage,
  },
  {
    path: "/disciplinas",
    name: "DisciplinaList",
    component: DisciplinaList,
  },
  {
    path: "/disciplinas/nova",
    name: "DisciplinaForm",
    component: DisciplinaForm,
  },
  {
    path: "/disciplinas/editar/:id",
    name: "DisciplinaEdit",
    component: DisciplinaForm,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
