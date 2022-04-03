
<template>
  <section id="app">
    <div v-for="film in films" :key="film.message">
      <p>{{film}}</p>
    </div>
  </section>
</template>

<script>
  export default {
    name :"f" ,
    data(){
      return{
        films:["Dune","Fast and Furious","Batman","Joker","Mad Max","Drive","Sherlock Holmes","Interstellar","Gladiator"]
      }
    }
  }
</script>

<style scoped>

    #app{
        background-color: #473f5a;
        color: white;
        font-family: Arial, Helvetica, sans-serif;
        font-weight: bold;  
    }



</style>
