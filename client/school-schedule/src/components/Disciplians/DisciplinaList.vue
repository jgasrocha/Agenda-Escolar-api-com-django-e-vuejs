<template>
  <div class="disciplinas-list">
    <h1>Lista de Disciplinas</h1>

    <!-- Botão para criar nova disciplina -->
    <div class="botao-criar">
      <router-link to="/disciplinas/nova">
        <button class="btn-criar">Criar Nova Disciplina</button>
      </router-link>
    </div>

    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Professor</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="disciplina in disciplinas" :key="disciplina.id">
          <td>{{ disciplina.id }}</td>
          <td>{{ disciplina.nome }}</td>
          <td>{{ disciplina.professor_nome }}</td>
          <td>
            <button @click="abrirModal(disciplina.id)">Editar</button>
            <button @click="deletarDisciplina(disciplina.id)">Deletar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal -->
    <div v-if="modalVisivel" class="modal-overlay" @click="fecharModal">
      <div class="modal" @click.stop>
        <DisciplinaEdit 
          :id="disciplina.id" 
          :nome="disciplina.nome" 
          :professor_nome="disciplina.professor_nome" 
          @salvar="atualizarDisciplina" 
          @fechar="fecharModal" 
        />
      </div>
    </div>
  </div>
</template>

<script>
import api from '../../api';
import DisciplinaEdit from './DisciplinaEdit.vue';

export default {
  components: { DisciplinaEdit },
  data() {
    return {
      disciplinas: [],
      modalVisivel: false,
      disciplina: {
        id: null,
        nome: '',
        professor_nome: '',  // Mudança aqui
      },
    };
  },
  created() {
    this.carregarDisciplinas();
  },
  methods: {
    async carregarDisciplinas() {
      try {
        const response = await api.get('/disciplinas/');
        this.disciplinas = response.data;
      } catch (error) {
        console.error('Erro ao carregar disciplinas.', error);
      }
    },
    abrirModal(id) {
      const disciplina = this.disciplinas.find(d => d.id === id);
      if (disciplina) {
        this.disciplina = { ...disciplina };
        this.modalVisivel = true;
      }
    },
    fecharModal() {
      this.modalVisivel = false;
    },
    async deletarDisciplina(id) {
      if (confirm('Deseja realmente deletar esta disciplina?')) {
        try {
          await api.delete(`/disciplinas/${id}/`);
          alert('Disciplina deletada com sucesso!'); // Alerta de sucesso
          this.carregarDisciplinas(); // Atualiza a lista de disciplinas
        } catch (error) {
          alert('Erro ao deletar disciplina.'); // Alerta de erro
          console.error('Erro ao deletar disciplina.', error);
        }
      }
    },
    async atualizarDisciplina(disciplinaAtualizada) {
      try {
        await api.put(`/disciplinas/${disciplinaAtualizada.id}/`, disciplinaAtualizada);
        alert('Disciplina atualizada com sucesso!'); // Alerta de sucesso
        this.carregarDisciplinas();
        this.fecharModal();
      } catch (error) {
        alert('Erro ao atualizar disciplina.'); // Alerta de erro
        console.error('Erro ao atualizar disciplina.', error);
      }
    },
  },
};
</script>

<style scoped>
.botao-criar {
  margin-bottom: 20px;
  text-align: right;
}

.btn-criar {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  border-radius: 5px;
}

.btn-criar:hover {
  background-color: #45a049;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

table th, table td {
  padding: 10px;
  text-align: left;
}

table th {
  background-color: #f2f2f2;
}

button {
  padding: 5px 10px;
  margin-right: 5px;
  cursor: pointer;
  border-radius: 5px;
}

button:hover {
  background-color: #f1f1f1;
}
</style>
