<template>
  <form @submit.prevent="salvar">
    <div>
      <label for="nome">Nome:</label>
      <input type="text" v-model="disciplina.nome" required />
    </div>

    <div>
      <label for="professor">Professor:</label>
      <select v-model="disciplina.professor_id" required>
        <option disabled value="">Selecione um professor</option>
        <option v-for="professor in professores" :key="professor.id" :value="professor.id">
          {{ professor.nome }}
        </option>
      </select>
    </div>

    <div v-if="erro" class="erro">{{ erro }}</div>
    <div v-if="sucesso" class="sucesso">{{ sucesso }}</div>

    <button type="submit">Salvar</button>
    <button type="button" @click="fecharModal">Fechar</button>
  </form>
</template>

<script>
import api from "../../api";

export default {
  props: {
    id: Number, 
    nome: String, 
    professor_id: Number, 
  },
  data() {
    return {
      disciplina: {
        id: this.id,
        nome: this.nome,
        professor_id: this.professor_id || "", 
      },
      professores: [],
      erro: "",
      sucesso: "",
    };
  },
  created() {
    this.carregarProfessores();
  },
  methods: {
    async carregarProfessores() {
      try {
        const response = await api.get("/professores/");
        this.professores = response.data;
      } catch (error) {
        console.error("Erro ao carregar professores:", error);
      }
    },
    async salvar() {
      try {
        const response = await api.put(`/disciplinas/${this.disciplina.id}/`, this.disciplina);
        const disciplinaAtualizada = response.data;
        this.sucesso = `Disciplina ${disciplinaAtualizada.nome} editada com sucesso.`;
        this.$emit("salvar", disciplinaAtualizada);
        this.fecharModal();
      } catch (error) {
        this.erro = `Erro: ${error.response?.data?.detail || error.message || "Erro desconhecido"}`;
      }
    },
    fecharModal() {
      this.$emit("fechar");
    }
  },
};
</script>
