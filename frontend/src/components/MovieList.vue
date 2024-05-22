<script setup>
    import { ref, onMounted } from 'vue';
    import axios from 'axios';
    import { RouterLink } from 'vue-router';

    

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
    <div class="movie-list-container">
        <h1>Movies</h1>
        <ul class="movie-list">
            <li v-for="movie in movies" :key="movie.id" class="movie-item">
                <router-link :to="{ name: 'MovieDetail', params: { id: movie.id } }" class="movie-link">{{ movie.title }}</router-link>
            </li>
        </ul>
        <button @click="prevPage" :disabled="!pagination.previous" class="pagination-button">Previous</button>
        <button @click="nextPage" :disabled="!pagination.next" class="pagination-button">Next</button>
    </div>
</template>

<style scoped>
    .movie-list-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    h1 {
        font-size: 24px;
        margin-bottom: 20px;
    }

    .movie-list {
        list-style-type: none;
        padding: 0;
    }

    .movie-item {
        margin-bottom: 10px;
    }

    .movie-link {
        color: #007bff;
        text-decoration: none;
        font-weight: bold;
    }

    .pagination-button {
        padding: 8px 16px;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin-right: 10px;
    }

    .pagination-button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
    }
</style>