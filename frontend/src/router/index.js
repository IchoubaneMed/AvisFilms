import { createRouter, createWebHistory } from 'vue-router';
import MovieList from '../components/MovieList.vue';
import MovieDetail from '../components/MovieDetail.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [ 
        {
            path: '/',
            name: 'MovieList',
            component: MovieList
          },
          {
            path: '/movies/:id',
            name: 'MovieDetail',
            component: MovieDetail,
            props: true
          }
    ]
});

export default router;
