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
        <button v-on:click='redirectToVote()' :disabled='selected<2'>
            Start Judging
        </button>
    </div>
</template>

<script>


export default {
    name: 'SelectFoods',
    data() {
        return {
            foods: [],
            selected: 0
        }
    },
    created() {
        this.loadFoods();
    },
    methods: {
        selectFood(index) {
            this.foods[index].selected = !this.foods[index].selected;
            if (this.foods[index].selected) {
                this.selected++;
            } else {
                this.selected--;
            }
            this.$http.post('api/selected_food', {foods: this.foods});
        },
        loadFoods() {
            this.$http.get('api/foods').then((response) => {
                this.foods = response.data;
                this.updateCount();
            })
        },
        updateCount() {
            this.selected = 0;
            for (var i=0; i<this.foods.length; i++) {
                if (this.foods[i].selected) {
                    this.selected++;
                }
            }
        },
        redirectToVote() {
            this.$router.push('vote');
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

button {
    padding: 7px;
    font-size: 25px;
}
</style>
