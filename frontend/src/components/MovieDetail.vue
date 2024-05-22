<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import ReviewForm from './ReviewForm.vue';
import { useRoute } from 'vue-router';

const router = useRoute();

const movie = ref({});

const selectedActors = ref([]);
const allActors = ref([]);

const fetchActors = async (url) => {
    const actorsResponse = await axios.get(url);
    const actorsData = actorsResponse.data;
    const nextPageUrl = actorsData.next;
    if (nextPageUrl) {
        const nextPageActors = await fetchActors(nextPageUrl);
        return [...actorsData.results, ...nextPageActors];
    } else {
        return actorsData.results;
    }

};


const fetchMovie = async () => {
    const response = await axios.get(`http://localhost:8000/api/v1/movies/${router.params.id}/`);
    movie.value = response.data;

    selectedActors.value = movie.value.actors.map(actor => actor);
    const allActorsData = await fetchActors('http://localhost:8000/api/v1/actors/');

    allActors.value = allActorsData;


}

const updateMovie = async () => {

    const actors = selectedActors.value.map(actorId => allActors.value.find(actor => actor.id === actorId));
    const actorIds = actors.map(actor => actor.id);

    await axios.put(`http://localhost:8000/api/v1/movies/${router.params.id}/`, { ...movie.value, actors: actorIds });


    fetchMovie();
}
onMounted(fetchMovie);


</script>

<template>
    <div class="movie-detail">
        <div class="title-container">
            <h1 class="title">{{ movie.title }}</h1>
            <router-link to="/" class="home-button">Go to Homepage</router-link>
        </div>
        <p class="description">{{ movie.description }}</p>
        <ul class="actors-list">
            <li v-for="actor in movie.actors" :key="actor.id">{{ actor.first_name }} {{ actor.last_name }}</li>
        </ul>
        <p class="average-review">Average Review: {{ movie.average }}</p>


        <h2 class="edit-title">Edit Movie</h2>
        <form @submit.prevent="updateMovie" class="edit-form">
            <label for="description">Description</label>
            <textarea id="description" v-model="movie.description" class="description-input"></textarea>
            <label for="actors">Actors (select multiple):</label>

            <select id="actors" v-model="selectedActors" multiple class="actors-input">
                <option v-for="actor in allActors" :key="actor.id" :value="actor.id">{{ actor.first_name }} {{
                    actor.last_name }}</option>
            </select>

            <button type="submit" class="save-button">Save</button>
        </form>


        <h2 class="add-review-title">Add Review</h2>
        <ReviewForm :movieId="movie.id" />
    </div>
</template>

<style scoped>
.title-container {
    display: flex;
    justify-content: space-between; 
    align-items: baseline; 
}
.home-button {
    display: block;
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    text-decoration: none;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.home-button:hover {
    background-color: #0056b3;
}

.movie-detail {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.title {
    font-size: 24px;
    margin-bottom: 10px;
}

.description {
    margin-bottom: 15px;
}

.actors-list {
    list-style-type: none;
    padding: 0;
}

.actor {
    margin-bottom: 5px;
}

.average-review {
    margin-top: 15px;
    font-weight: bold;
}

.edit-title,
.add-review-title {
    margin-top: 30px;
    font-size: 20px;
}

.edit-form {
    margin-top: 15px;
}

.description-input,
.actors-input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
}

.save-button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.save-button:hover {
    background-color: #0056b3;
}
</style>