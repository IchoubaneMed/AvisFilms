<script setup>
import { ref, defineProps, defineEmits } from 'vue';
import axios from 'axios';

const grade = ref(0);

const props = defineProps(['movieId']);
const { emit } = defineEmits(['review-added']);

const addReview = async () => {
    await axios.post(`http://localhost:8000/api/v1/movies/${props.movieId}/review/`, { grade: grade.value, movie: props.movieId });
    emit('review-added');
}

</script>

<template>
    <form @submit.prevent="addReview">
        <label>Grade:</label>
        <input type="number" v-model="grade" min="1" max="5" required />
        <button type="submit">Submit</button>
    </form>
</template>