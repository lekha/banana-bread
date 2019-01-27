<template>
    <div class='main'>
        <h1>Which banana foods have you sampled?</h1>
        <div class='icon-list'>
            <div class='icon-wrapper' v-for='(food, index) in foods' :key='index'>
                <img class='icon' v-bind:src='food.image_url'>
                <p>{{ food.owner }}'s</p>
            </div>
        </div>
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
                    'image_url': 'https://www.simplyrecipes.com/wp-content/uploads/2014/08/banana-bread-vertical-c-1200.jpg'
                },
                {
                    'owner': 'Mike K',
                    'image_url': 'https://images-gmi-pmc.edge-generalmills.com/c23f59e1-1a55-4ba7-91de-71ca24e197fe.jpg'
                },
                {
                    'owner': 'Danielle',
                    'image_url': 'https://www.landolakes.com/RecipeManagementSystem/media/Recipe-Media-Files/Recipes/Retail/x17/20643-walnut-banana-bread-600x600.jpg?ext=.jpg'
                }
            ]
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
}

.icon {
    display: block;
    height: 230px;
    width: 230px;
    border: 15px solid;
    border-radius: 10px;
    margin: 15px -7.5px -15px -7.5px;
}
</style>
