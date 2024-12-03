<template>
    <div id="app">
      <div class="table-container">
        <!-- Tabela para dispositivos maiores (desktop e tablet) -->
        <table border="1" v-if="!isMobile">
          <thead>
            <tr>
              <th v-for="coluna in colunas" :key="coluna">{{ coluna }}</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td v-for="coluna in colunas" :key="coluna">
                <div class="cards-container">
                  <div class="card" v-for="i in 10" :key="i">
                    <p>Dia: {{ coluna }} - Card {{ i }}</p>
                  </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
  
        <!-- Exibição no celular como slide -->
        <div v-else class="mobile-slide">
          <div class="cards-container">
            <h3>{{ colunas[colunaAtiva] }}</h3>
            <div class="card" v-for="i in 10" :key="i">
              <p>Dia: {{ colunas[colunaAtiva] }} - Card {{ i }}</p>
            </div>
          </div>
          <div class="navigation-buttons">
            <button @click="mudarDia(-1)" :disabled="colunaAtiva === 0">
              &#8592; Anterior
            </button>
            <button @click="mudarDia(1)" :disabled="colunaAtiva === colunas.length - 1">
              Próximo &#8594;
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        colunas: ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"], // Dias da semana
        colunaAtiva: 0, // Índice do dia ativo no modo mobile
        isMobile: window.innerWidth <= 768, // Verifica se o dispositivo é mobile
      };
    },
    mounted() {
      this.atualizarDiaAtivo(); // Define o dia atual na inicialização
      window.addEventListener("resize", this.handleResize);
    },
    beforeDestroy() {
      window.removeEventListener("resize", this.handleResize);
    },
    methods: {
      handleResize() {
        this.isMobile = window.innerWidth <= 768;
      },
      atualizarDiaAtivo() {
        const hoje = new Date();
        const diaSemana = hoje.getDay(); // Domingo = 0, Segunda = 1, ..., Sábado = 6
        this.colunaAtiva = diaSemana === 0 ? 5 : diaSemana - 1; // Ajusta domingo para sábado
      },
      mudarDia(direcao) {
        this.colunaAtiva = Math.min(
          Math.max(0, this.colunaAtiva + direcao),
          this.colunas.length - 1
        );
      },
    },
  };
  </script>
  
  <style scoped>
  .table-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
  }
  table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
  }
  th,
  td {
    text-align: center;
    padding: 10px;
    border: 1px solid #ccc;
  }
  .card {
    border: 1px solid #ccc;
    padding: 10px;
    background-color: #f4f4f4;
    border-radius: 5px;
    margin: 5px 0;
  }
  .cards-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
  }
  .navigation-buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 10px;
  }
  .navigation-buttons button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  /* Estilo para o modo mobile */
  .mobile-slide {
    text-align: center;
    margin-top: 20px;
  }
  .mobile-slide .cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Define o tamanho mínimo */
  gap: 10px; /* Espaçamento uniforme entre os cartões */
  justify-items: center; /* Centraliza os cartões dentro das células */
  width: 100%; /* Garante que ocupe a largura disponível */
  margin: 0 auto; /* Centraliza a grade na tela */
}

.card {
  width: 100%; /* Garante que os cartões tenham o mesmo tamanho */
  max-width: 140px; /* Limita a largura máxima dos cartões */
  text-align: center; /* Centraliza o texto dentro do cartão */
}
  h3 {
    margin-bottom: 20px;
  }
  </style>
  