<template>
    <div class='main'>
        <h1>Which banana foods have you sampled?</h1>
        <div class='icon-list'>
            <div class='icon-wrapper' v-for='(food, index) in foods' :key='index' v-on:click='selectFood(index)'>
                <img class='icon' v-bind:src='food.image_url'>
                <transition name='fade'>
                    <div class='overlay' v-if='food.selected'><i class='fas fa-check fa-5x'></i></div>
                </transition>
                <p>{{ food.owner }}'s</p>
            </div>
        </div>
        <button>Start Judging</button>
    </div>
</template>

<script>
export default {
    name: 'SelectFoods',
    data() {
        return {
            foods: [
                {
                    'owner': 'Lekha',
                    'image_url': 'https://www.simplyrecipes.com/wp-content/uploads/2014/08/banana-bread-vertical-c-1200.jpg',
                    'selected': false
                },
                {
                    'owner': 'Mike K',
                    'image_url': 'https://images-gmi-pmc.edge-generalmills.com/c23f59e1-1a55-4ba7-91de-71ca24e197fe.jpg',
                    'selected': false
                },
                {
                    'owner': 'Danielle',
                    'image_url': 'https://www.landolakes.com/RecipeManagementSystem/media/Recipe-Media-Files/Recipes/Retail/x17/20643-walnut-banana-bread-600x600.jpg?ext=.jpg',
                    'selected': false
                }
            ]
        }
    },
    methods: {
        selectFood(index) {
            this.foods[index].selected = !this.foods[index].selected;
        }
    }
}
</script>

<style scoped>
@import 'https://use.fontawesome.com/releases/v5.6.3/css/all.css';

.main {
    width: 90%;
    margin-left: auto;
    margin-right: auto;
}

h1 {
    font-weight: normal;
    line-height: 1.1;
}

.icon-wrapper {
    display: inline-block;
    height: 260px;
    position: relative;
}

.icon {
    display: block;
    height: 230px;
    width: 230px;
    border: 15px solid;
    border-radius: 10px;
    margin: 15px -7.5px -15px -7.5px;
}

.icon:hover {
    filter: brightness(120%);
}

.overlay {
    position: absolute;
    top: 15px;
    left: -7.5px;
    height: 230px;
    width: 230px;
    display: grid;
    align-items: center;
    color: #50CB78;
    background-color: rgba(127, 127, 127, 0.5);
    background-clip: padding-box;
    transition: 2s ease;
    border: 15px solid rgba(0, 0, 0, 0);
    border-radius: 10px;
}

.fade-enter-active, .fade-leave-active {
    transition: opacity 0.3s;
}

.fade-enter, .fade-leave-to {
    opacity: 0;
}
</style>
