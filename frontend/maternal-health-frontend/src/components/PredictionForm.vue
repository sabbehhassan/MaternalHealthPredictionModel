<template>
    <div class="form-container">
      <h2>Enter Patient Details</h2>
      <form @submit.prevent="predict">
        <label>Age:</label>
        <input type="number" v-model="form.age" required />
  
        <label>Systolic BP:</label>
        <input type="number" v-model="form.systolic_bp" required />
  
        <label>Diastolic BP:</label>
        <input type="number" v-model="form.diastolic_bp" required />
  
        <label>Blood Sugar:</label>
        <input type="number" v-model="form.blood_sugar" required />
  
        <label>Body Temperature:</label>
        <input type="number" v-model="form.body_temp" required />
  
        <label>Heart Rate:</label>
        <input type="number" v-model="form.heart_rate" required />
  
        <button type="submit">Predict</button>
      </form>
  
      <div v-if="prediction">
        <h3>Prediction Result:</h3>
        <p>{{ prediction }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        form: {
          age: "",
          systolic_bp: "",
          diastolic_bp: "",
          blood_sugar: "",
          body_temp: "",
          heart_rate: "",
        },
        prediction: null,
      };
    },
    methods: {
      async predict() {
        try {
          const response = await axios.post("http://127.0.0.1:5000/predict", this.form);
          this.prediction = response.data.prediction;
        } catch (error) {
          console.error("Error fetching prediction:", error);
        }
      },
    },
  };
  </script>
  
  <style>
  .form-container {
    width: 300px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  input {
    width: 100%;
    padding: 5px;
    margin-bottom: 10px;
  }
  button {
    width: 100%;
    padding: 8px;
    background: blue;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
  