<!-- src/components/AdminList.vue -->
<template>
    <div class="admin-list">
      <h1>Lista de Administradores</h1>
      <table>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Email</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="admin in administradores" :key="admin.id">
            <td>{{ admin.nome }}</td>
            <td>{{ admin.email }}</td>
            <td>
              <router-link :to="{ name: 'editarProfessor', params: { id: admin.id } }">Editar</router-link>
            </td>
          </tr>
        </tbody>
      </table>
      <div v-if="mensagem" :class="mensagemClasse">{{ mensagem }}</div>
    </div>
  </template>
  
  <script>
  import api from '../../api'; // Importando a instância do axios
  
  export default {
    data() {
      return {
        administradores: [],
        mensagem: '',
        mensagemClasse: '',
      };
    },
    created() {
      this.carregarAdministradores(); // Carregar a lista de administradores ao criar o componente
    },
    methods: {
      async carregarAdministradores() {
        try {
          const response = await api.get('/professores/?is_admin=true'); // Ajuste a URL conforme necessário
          this.administradores = response.data;
        } catch (error) {
          console.error('Erro ao carregar administradores:', error);
          this.mensagem = 'Erro ao carregar a lista de administradores.';
          this.mensagemClasse = 'error';
        }
      },
    },
  };
  </script>
  
  <style>
  .admin-list {
    margin: 20px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
  }
  th {
    background-color: #f2f2f2;
  }
  </style>
  