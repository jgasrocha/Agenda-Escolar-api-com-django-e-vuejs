<template>
  <form @submit.prevent="salvar">
    <div>
      <label for="nome">Nome:</label>
      <input type="text" id="nome" v-model="professor.nome" required />
    </div>
    <div>
      <label for="email">Email:</label>
      <input type="email" id="email" v-model="professor.email" required />
    </div>
    <div>
      <label for="admin">Admin:</label>
      <select v-model="professor.is_admin" id="admin">
        <option :value="true">Torna Admin</option>
        <option :value="false">Não é Admin</option>
      </select>
    </div>
    <div>
      <button type="submit">Salvar</button>
      <button type="button" @click="fecharModal">Fechar</button>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    id: {
      type: Number,
      required: true,
    },
    nome: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
    },
    is_admin: {
      type: Boolean,
      required: false,
    },
  },
  data() {
    return {
      professor: {
        id: this.id,
        nome: this.nome,
        email: this.email,
        is_admin: this.is_admin, // Estado inicial do select
      },
    };
  },
  created() {
    // Verifica se o professor é admin quando o componente for criado
    this.verificarSeAdmin();
  },
  methods: {
    async verificarSeAdmin() {
      try {
        // Faz a requisição para verificar se o professor é admin
        const response = await axios.get(`/api/is_professor_admin/${this.professor.id}/`);
        console.log('Resposta da API:', response); // Log da resposta para depuração
        // Atualiza o estado do select com base na resposta da API
        this.professor.is_admin = response.data.is_admin;
      } catch (error) {
        console.error('Erro ao verificar admin:', error);
      }
    },
    async salvar() {
      console.log('Salvando professor:', this.professor); // Verifica o estado antes de salvar
      try {
        if (this.professor.is_admin) {
          // Se is_admin for true, torna o professor admin
          await axios.post('/api/admins/', { professor: this.professor.id });
        } else {
          // Se is_admin for false, remove o admin
          await axios.delete(`/api/admins/${this.professor.id}/`);
        }
        this.$emit('salvar', this.professor); // Passa os dados atualizados
        console.log('Professor salvo com sucesso'); // Log de sucesso
      } catch (error) {
        console.error('Erro ao salvar:', error);
      }
    },
    fecharModal() {
      // Emitir evento para fechar o modal
      this.$emit('fechar');
    },
  },
};
</script>

<style scoped>
/* Estilos para o formulário de edição */
form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}
label {
  font-weight: bold;
}
input,
select {
  padding: 10px;
  margin: 5px 0;
  border-radius: 4px;
  border: 1px solid #ddd;
}
button {
  padding: 10px;
  margin-top: 10px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
</style>
