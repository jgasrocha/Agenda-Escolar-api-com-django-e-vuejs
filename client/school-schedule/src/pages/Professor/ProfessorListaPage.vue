<!-- src/pages/ProfessoresPage.vue -->
<template>
    <div>
      <ListaProfessores />
    </div>
  </template>
  
  <script>
  import ListaProfessores from '../../components/Professor/ProfessorList.vue'; // Ajuste o caminho conforme necessário
  
  export default {
    components: {
      ListaProfessores,
    },
  };
  </script>
  
  <style>
  /* Estilos adicionais para a página, se necessário */
  </style>
  