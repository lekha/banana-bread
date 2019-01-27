import Vue from 'vue';
import Router from 'vue-router';
import SelectUser from '@/components/SelectUser.vue';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'SelectUser',
            component: SelectUser
        }
    ]
});
