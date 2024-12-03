<template>
  <div class="disciplina-edit-page">
    <DisciplinaEdit 
      :id="disciplina.id"
      :nome="disciplina.nome"
      :descricao="disciplina.descricao"
    />
  </div>
</template>

<script>
import DisciplinaEdit from '../../components/Disciplians/DisciplinaEdit.vue';

export default {
  components: {
    DisciplinaEdit
  },
  data() {
    return {
      disciplina: {
        id: 1, // exemplo de ID
        nome: '',
        descricao: ''
      }
    };
  },
  created() {
    // Aqui você pode buscar a disciplina pelo ID, usando API, por exemplo
    this.carregarDisciplina();
  },
  methods: {
    async carregarDisciplina() {
      try {
        const response = await this.$api.get(`/disciplinas/${this.disciplina.id}`);
        this.disciplina = response.data;
      } catch (error) {
        console.error('Erro ao carregar a disciplina');
      }
    }
  }
};
</script>
