<template>
  <div>
    <h1>{{ isEdit ? 'Editar Disciplina' : 'Nova Disciplina' }}</h1>
    <DisciplinaForm :professores="professores" :disciplinaEditar="disciplinaEditar" @salvar="criarDisciplina" />
  </div>
</template>

<script>
import DisciplinaForm from "../../components/Disciplians/DisciplinaForm.vue";
import api from "../../api";

export default {
  components: { DisciplinaForm },
  data() {
    return {
      professores: [],
      disciplinaEditar: null, // Para editar, passamos os dados da disciplina
    };
  },
  methods: {
    async fetchProfessores() {
      try {
        const response = await api.get("/professores/");
        this.professores = response.data;
      } catch (error) {
        console.error("Erro ao carregar professores:", error);
      }
    },
    async fetchDisciplina() {
      try {
        const response = await api.get(`/disciplinas/${this.$route.params.id}/`);
        this.disciplinaEditar = response.data;
      } catch (error) {
        console.error("Erro ao carregar disciplina:", error);
      }
    },
    async criarDisciplina(disciplina) {
      await api.post("/disciplinas/", disciplina);
      this.$router.push({ name: "Disciplinas" });
    },
  },
  created() {
    this.fetchProfessores();
    if (this.$route.params.id) {
      this.fetchDisciplina();
    }
  },
};
</script>
