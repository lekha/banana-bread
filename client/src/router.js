import Vue from 'vue';
import Router from 'vue-router';
import SelectRole from '@/components/SelectRole.vue';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'SelectRole',
            component: SelectRole
        }
    ]
});
