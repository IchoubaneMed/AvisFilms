<script setup>
    import { ref, onMounted } from 'vue';
    import axios from 'axios';

    const movies = ref([]);
    const pagination = ref({});
    const fetchMovies = async (url = 'http://localhost:8000/api/v1/movies/') => {
        const response = await axios.get(url);
        movies.value = response.data.results;
        pagination.value = response.data;
    };

    const prevPage = () => {
        if (pagination.value.previous) {
            fetchMovies(pagination.value.previous);
        }
    };

    const nextPage = () => {
        if (pagination.value.next) {
            fetchMovies(pagination.value.next);
        }
    };

    onMounted(fetchMovies);
</script>


<template>
    <div>
        <h1>Movie</h1>
        <ul>
            <li v-for="movie in movies" :key="movie.id">
                
                <h1>{{ movie.title }}</h1>
            </li>
        </ul>
        <button @click="prevPage" :disabled="!pagination.previous">Previous</button>
        <button @click="nextPage" :disabled="!pagination.next">Next</button>
    </div>
</template>

