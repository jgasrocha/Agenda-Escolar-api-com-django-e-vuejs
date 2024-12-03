<template>
    <div class="admin-form">
      <h1>Designar Professor como Admin</h1>
      <form @submit.prevent="criarAdmin">
        <div class="form-group">
          <label for="professor">Escolha o Professor:</label>
          <select v-model="selectedProfessor" required>
            <option v-for="professor in professores" :key="professor.id" :value="professor.id">
              {{ professor.nome }}
            </option>
          </select>
        </div>
        <button type="submit" class="btn">Designar como Admin</button>
      </form>
      <div v-if="mensagem" :class="mensagemClasse">{{ mensagem }}</div>
    </div>
  </template>
  
  <script>
  import api from '../../api';  // Importando a instância do axios
  
  export default {
    data() {
      return {
        selectedProfessor: null,  // Campo para armazenar o professor selecionado
        professores: [],
        mensagem: '',
        mensagemClasse: '',
      };
    },
    created() {
      this.carregarProfessores();  // Carregar professores ao criar o componente
    },
    methods: {
      async carregarProfessores() {
        try {
          const response = await api.get('/professores/');  // Ajuste a URL conforme necessário
          this.professores = response.data;
        } catch (error) {
          console.error('Erro ao carregar professores:', error);
        }
      },
      async criarAdmin() {
        try {
          const response = await api.post('/admins/', { professor: this.selectedProfessor }); // Armazena a resposta
          const professorNome = response.data.professor_nome; // Acesso correto à variável
          this.mensagem = `Professor ${professorNome} designado como admin com sucesso!`;
          this.mensagemClasse = 'success';
          this.resetForm();
        } catch (error) {
          this.mensagem = 'Erro ao designar professor como admin: ' + (error.response.data.detail || 'Erro desconhecido');
          this.mensagemClasse = 'error';
        }
      },
      resetForm() {
        this.selectedProfessor = null;  // Resetando a seleção do professor
      },
    },
  };
  </script>
  
  
  <style lang="css" scoped>
  .admin-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  
  .admin-form h1 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
  }
  
  .admin-form .form-group {
    margin-bottom: 15px;
  }
  
  .admin-form .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #555;
  }
  
  .admin-form .form-group select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
  }
  
  .admin-form .form-group select:focus {
    border-color: #007bff;
    outline: none;
  }
  
  .admin-form .btn {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .admin-form .btn:hover {
    background-color: #0056b3;
  }
  
  .admin-form .success {
    color: green;
    text-align: center;
    margin-top: 15px;
  }
  
  .admin-form .error {
    color: red;
    text-align: center;
    margin-top: 15px;
  }
  </style>
  