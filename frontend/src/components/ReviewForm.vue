<script setup>
import { ref, defineProps, defineEmits } from 'vue';
import axios from 'axios';

const grade = ref(0);

const props = defineProps(['movieId']);

const addReview = async () => {
    
    await axios.post(`http://localhost:8000/api/v1/movies/${props.movieId}/review/`, { grade: grade.value, movie: props.movieId });
    
}

</script>

<template>
    <form @submit.prevent="addReview" class="review-form">
        <label for="grade" class="label">Grade:</label>
        <input id="grade" type="number" v-model="grade" min="1" max="5" required class="input"/>
        <button type="submit" class="submit-button">Submit</button>
    </form>
</template>

<style scoped>
.review-form {
    margin-top: 20px;
}
.label {
    font-weight: bold;
    margin-bottom: 10px;
    display: block;
}
.input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 15px;
}
.submit-button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.submit-button:hover {
    background-color: #0056b3;
}

</style>