<template>
    <div class="professor-form">
      <h1>Criar Professor</h1>
      <form @submit.prevent="criarProfessor">
        <div class="form-group">
          <label for="nome">Nome:</label>
          <input type="text" v-model="professor.nome" required />
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" v-model="professor.email" required />
        </div>
        <div class="form-group">
          <label for="senha">Senha:</label>
          <input type="password" v-model="professor.senha" required />
        </div>
        <button type="submit" class="btn">Criar Professor</button>
      </form>
      <div v-if="mensagem" :class="mensagemClasse">{{ mensagem }}</div>
    </div>
  </template>
  
  <script>
  import api from '../../api';
  
  export default {
    data() {
      return {
        professor: {
          nome: '',
          email: '',
          senha: '',
        },
        mensagem: '',
        mensagemClasse: '',
      };
    },
    methods: {
      async criarProfessor() {
        try {
          await api.post('/professores/', this.professor);
          this.mensagem = 'Professor criado com sucesso!';
          this.mensagemClasse = 'success';
          this.resetForm();
        } catch (error) {
          this.mensagem = 'Erro ao criar professor: ' + (error.response.data.detail || 'Erro desconhecido');
          this.mensagemClasse = 'error';
        }
      },
      resetForm() {
        this.professor.nome = '';
        this.professor.email = '';
        this.professor.senha = '';
      },
    },
  };
  </script>
  
  <style lang="css" scoped>
  .professor-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  
  .professor-form h1 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
  }
  
  .professor-form .form-group {
    margin-bottom: 15px;
  }
  
  .professor-form .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #555;
  }
  
  .professor-form .form-group input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
  }
  
  .professor-form .form-group input:focus {
    border-color: #007bff;
    outline: none;
  }
  
  .professor-form .btn {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .professor-form .btn:hover {
    background-color: #0056b3;
  }
  
  .professor-form .success {
    color: green;
    text-align: center;
    margin-top: 15px;
  }
  
  .professor-form .error {
    color: red;
    text-align: center;
    margin-top: 15px;
  }
  </style>
  