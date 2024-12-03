<template>
    <div>
      <h1>Agenda Semanal</h1>
      <AgendaComponent />
    </div>
  </template>
  
  <script>
  import AgendaComponent from '../../components/Agenda/AgendaComponent.vue';
  
  export default {
    components: {
      AgendaComponent,
    },
  };
  </script>
  
  <style scoped>
  /* Estilos específicos para a página da agenda */
  </style>
  