import Vue from 'vue';
import Router from 'vue-router';
import SelectRole from '@/components/SelectRole.vue';
import SelectFoods from '@/components/SelectFoods.vue';
import Vote from '@/components/Vote.vue';
import Leaderboard from '@/components/Leaderboard.vue';
import Photo from '@/components/Photo.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'SelectRole',
            component: SelectRole
        },
        {
            path: '/select',
            name: 'SelectFoods',
            component: SelectFoods
        },
        {
            path: '/vote',
            name: 'Vote',
            component: Vote 
        },
        {
            path: '/leaderboard',
            name: 'Leaderboard',
            component: Leaderboard
        },
        {
            path: '/upload',
            name: 'Photo',
            component: Photo
        }
    ]
});
