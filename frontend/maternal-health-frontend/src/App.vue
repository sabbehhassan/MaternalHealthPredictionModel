<template>
  <div id="app">
    <h1>Maternal Health Prediction</h1>
    <PredictionForm />
  </div>
</template>

<script>
import PredictionForm from "./components/PredictionForm.vue";

export default {
  components: {
    PredictionForm,
  },
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 20px;
}
</style>
