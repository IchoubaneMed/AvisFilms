<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import ReviewForm from './ReviewForm.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const movie = ref({});
const actorsInput = ref('');

const fetchMovie = async () => {
    const response = await axios.get(`http://localhost:8000/api/v1/movies/${$route.params.id}/`);
    movie.value = response.data;
    actorsInput.value = movie.value.actors.map(actor => `${actor.first_name} ${actor.last_name}`).join(', ');
}   

const updateMovie = async () => {
    const actors = actorsInput.value.split(',').map(name => {
        const [first_name, last_name] = name.trim().split(' ');
        return { first_name, last_name };
    })
    await axios.put(`http://localhost:8000/api/v1/movies/${$route.params.id}/`, { ...movie.value, actors });
    fetchMovie();
}
onMounted(fetchMovie);
</script>

<template>
    <div>
        <h1>{{ movie.title }}</h1>
        <p>{{ movie.description }}</p>
        <ul>
            <li v-for="actor in movie.actors" :key="actor.id">{{ actor.first_name }} {{ actor.last_name }}</li>
        </ul>
        <p>Average Review: {{ movie.average }}</p>
        <h2>Edit Movie</h2>
        <form @submit.prevent="updateMovie">
            <label>Description</label>
            <textarea v-model="movie.description"></textarea>
            <label>Actors (comma separated):</label>
            <input type="text" v-model="actorsInput"/>
            <button type="submit">Save</button>
        </form>
        <h2>Add Review</h2>
        <ReviewForm :movieId="movie.id" @review-added="fetchMovie" />
    </div>
</template>