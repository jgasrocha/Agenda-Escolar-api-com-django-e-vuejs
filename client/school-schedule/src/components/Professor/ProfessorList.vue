<template>
  <div class="professores-list">
    <h1>Lista de Professores</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Email</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="professor in professores" :key="professor.id">
          <td>{{ professor.id }}</td>
          <td>{{ professor.nome }}</td>
          <td>{{ professor.email }}</td>
          <td>
            <button @click="abrirModal(professor.id)">Editar</button>
            <button @click="deletarProfessor(professor.id)">Deletar</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="mensagem" :class="mensagemClasse">{{ mensagem }}</div>

    <!-- Modal -->
    <div v-if="modalVisivel" class="modal-overlay" @click="fecharModal">
      <div class="modal" @click.stop>
        <!-- Passando os dados do professor para o ProfessorEdit -->
        <ProfessorEdit 
          :id="professor.id" 
          :nome="professor.nome" 
          :email="professor.email" 
          :is_admin="professor.is_admin" 
          @salvar="atualizarProfessor" 
          @fechar="fecharModal" 
        />
      </div>
    </div>
  </div>
</template>

<script>
import api from '../../api'; // Importando a instância do axios
import ProfessorEdit from './ProfessorEdit.vue'; // Importando o componente ProfessorEdit

export default {
  components: {
    ProfessorEdit, // Registrando o componente ProfessorEdit
  },
  data() {
    return {
      professores: [],
      mensagem: '',
      mensagemClasse: '',
      modalVisivel: false, // Controle de visibilidade do modal
      professor: { // Dados do professor a ser editado
        id: null,
        nome: '',
        email: '',
        is_admin: false,
      },
    };
  },
  created() {
    this.carregarProfessores(); // Carregar professores ao criar o componente
  },
  methods: {
    async carregarProfessores() {
      try {
        const response = await api.get('/professores/'); // Ajuste a URL conforme necessário
        this.professores = response.data;
      } catch (error) {
        console.error('Erro ao carregar professores:', error);
        this.mensagem = 'Erro ao carregar a lista de professores.';
        this.mensagemClasse = 'error';
      }
    },
    async deletarProfessor(id) {
      if (confirm('Você tem certeza que deseja deletar este professor?')) {
        try {
          await api.delete(`/professores/${id}/`); // Ajuste a URL conforme necessário
          this.mensagem = 'Professor deletado com sucesso!';
          this.mensagemClasse = 'success';
          this.carregarProfessores(); // Recarregar a lista de professores
        } catch (error) {
          this.mensagem = 'Erro ao deletar professor: ' + (error.response.data.detail || 'Erro desconhecido');
          this.mensagemClasse = 'error';
        }
      }
    },
    abrirModal(id) {
      // Encontrar o professor pelo ID e preencher o estado 'professor'
      const professor = this.professores.find(p => p.id === id);
      if (professor) {
        this.professor = { ...professor }; // Preencher os dados do professor no estado
        this.modalVisivel = true; // Exibir o modal
      }
    },
    fecharModal() {
      this.modalVisivel = false; // Fechar o modal
    },
    async atualizarProfessor(professorAtualizado) {
      try {
        // Chamar a API para atualizar o professor
        await api.put(`/professores/${professorAtualizado.id}/`, professorAtualizado);
        this.mensagem = 'Professor atualizado com sucesso!';
        this.mensagemClasse = 'success';
        this.carregarProfessores(); // Recarregar a lista de professores
        this.fecharModal(); // Fechar o modal após atualização
      } catch (error) {
        console.error('Erro ao atualizar professor:', error);
        this.mensagem = 'Erro ao atualizar professor: ' + (error.response?.data?.detail || 'Erro desconhecido');
        this.mensagemClasse = 'error';
      }
    },
  },
};
</script>

<style>
/* Estilos do componente */
.professores-list {
  max-width: 1200px;
  margin: 0 auto;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}
th {
  background-color: #f4f4f4;
}
button {
  padding: 5px 10px;
  cursor: pointer;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
}
button:hover {
  background-color: #0056b3;
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.modal {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 500px;
  width: 100%;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
