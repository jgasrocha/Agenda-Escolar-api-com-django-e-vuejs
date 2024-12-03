<template>
  <div>
    <h2>{{ isEdit ? 'Editar' : 'Criar' }} Disciplina</h2>
    <form @submit.prevent="criarOuEditarDisciplina">
      <!-- Campo de nome da disciplina -->
      <div>
        <label for="nome">Nome da Disciplina:</label>
        <input
          id="nome"
          v-model="disciplina.nome"
          type="text"
          placeholder="Nome da Disciplina"
          required
        />
      </div>

      <!-- Campo de seleção do professor -->
      <div>
        <label for="professor">Selecione o Professor:</label>
        <select v-model="disciplina.professor_id" id="professor" required>
          <option v-for="professor in professores" :key="professor.id" :value="professor.id">
            {{ professor.nome }}
          </option>
        </select>
      </div>

      <!-- Botão de criação ou edição -->
      <div>
        <button type="submit">{{ isEdit ? 'Editar' : 'Criar' }} Disciplina</button>
      </div>
    </form>

    <!-- Mensagem de status -->
    <div :class="mensagemClasse" v-if="mensagem">
      {{ mensagem }}
    </div>
  </div>
</template>

<script>
import api from '../../api.js'; // Supondo que você tenha um arquivo api.js configurado

export default {
  data() {
    return {
      disciplina: {
        id: null,
        nome: '',
        professor_id: null
      },
      professores: [], // Lista de professores que será carregada da API
      isEdit: false, // Definido como falso para criação de disciplina
      mensagem: '',
      mensagemClasse: ''
    };
  },
  methods: {
    async carregarProfessores() {
      try {
        const response = await api.get('/professores/'); // A URL para obter os professores pode variar
        this.professores = response.data;
      } catch (error) {
        console.error('Erro ao carregar professores:', error);
        this.mensagem = 'Erro ao carregar professores.';
        this.mensagemClasse = 'error';
      }
    },

    async criarOuEditarDisciplina() {
      try {
        let response;
        console.log('Dados enviados para o backend:', this.disciplina);  // Verifique os dados

        if (this.isEdit) {
          // Editar a disciplina
          response = await api.put(`/disciplinas/${this.disciplina.id}/`, this.disciplina);
          this.mensagem = `Disciplina ${this.disciplina.nome} editada com sucesso!`;
        } else {
          // Criar nova disciplina
          response = await api.post("/disciplinas/", this.disciplina);
          this.mensagem = `Disciplina ${this.disciplina.nome} criada com sucesso!`;
        }

        this.mensagemClasse = 'success';
        this.$router.push({ name: "DisciplinaList" }); // Redireciona para a lista de disciplinas
      } catch (error) {
        console.error("Erro ao salvar disciplina:", error);
        this.mensagem = `Erro ao salvar disciplina: ${error.response?.data?.detail || error.message || 'Erro desconhecido'}`;
        this.mensagemClasse = 'error';
      }
    },

    // Função para configurar o formulário para edição
    editarDisciplina(id) {
      this.isEdit = true;
      this.carregarDisciplina(id);
    },

    // Carregar os dados da disciplina para edição
    async carregarDisciplina(id) {
      try {
        const response = await api.get(`/disciplinas/${id}/`);
        this.disciplina = response.data;
      } catch (error) {
        console.error("Erro ao carregar disciplina:", error);
        this.mensagem = 'Erro ao carregar os dados da disciplina';
        this.mensagemClasse = 'error';
      }
    }
  },
  created() {
    // Carregar os professores ao inicializar o componente
    this.carregarProfessores();

    // Se a página for de edição, você pode configurar a disciplina ao carregar o ID da URL
    const idDisciplina = this.$route.params.id; // Supondo que o ID da disciplina venha pela URL
    if (idDisciplina) {
      this.editarDisciplina(idDisciplina);
    }
  }
};
</script>

<style scoped>
/* Estilo básico para o formulário */
form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 400px;
  margin: 0 auto;
}

label {
  font-weight: bold;
}

input, select {
  padding: 10px;
  font-size: 16px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

button {
  padding: 10px;
  font-size: 16px;
  border: none;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
  border-radius: 4px;
}

button:hover {
  background-color: #45a049;
}

.success {
  color: green;
}

.error {
  color: red;
}
</style>
