<template>
    <div class='main'>
        <h1>Which one was <u>{{ superlative }}</u>?</h1>
        <div class='grid'>
            <p></p>
            <img class='icon' v-bind:src='food1.imageUrl'>
            <p class='icon-text'>vs.</p>
            <img class='icon' v-bind:src='food2.imageUrl'>
            <p></p>
            <p></p>
            <p>{{ food1.owner }}'s</p>
            <p></p>
            <p>{{ food2.owner }}'s</p>
            <p></p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Vote',
    data() {
        return {
            superlative: 'prettier',
            food1: {
                owner: 'Lekha',
                imageUrl: 'https://www.simplyrecipes.com/wp-content/uploads/2014/08/banana-bread-vertical-c-1200.jpg'
            },
            food2: {
                owner: 'Mike K',
                imageUrl: 'https://images-gmi-pmc.edge-generalmills.com/c23f59e1-1a55-4ba7-91de-71ca24e197fe.jpg' 
            }
        }
    }
}
</script>

<style scoped>
@import 'https://use.fontawesome.com/releases/v5.6.3/css/all.css';

.main {
    margin-left: auto;
    margin-right: auto;
    width: 90%;
    display: inline;
}

h1 {
    font-weight: normal;
    line-height: 1.1;
}

p {
    font-size: 50px;
    margin: 0;
}

.grid {
    display: grid;
    grid-template-columns: auto auto 150px auto auto;
    grid-template-rows: auto;
    align-items: center;
    justify-items: center;
}

#left-image {
    grid-area: left-image;
}

#middle {
    grid-area: middle;
}

#right-image {
    grid-area: right-image;
}

#left-text {
    grid-area: left-text;
}

#right-text {
    grid-area: right-text;
}

.icon {
    display: block;
    margin: 50px;
    height: 450px;
    width: 450px;
    border: solid 15px;
    border-radius: 10px;
    display: inline-block;
    filter: saturate(75%);
    transition: transform 0.2s, filter 0.2s, box-shadow 0.2s;
    box-shadow: 0 5px #CCCCCC;
}

.icon:hover {
    filter: saturate(100%);
    transform: scale(1.1);
}

.icon:active {
    transform: scale(1.1) translateY(5px);
    box-shadow: 0 0 #CCCCCC;
}

.icon-text {
    display: inline-block;
    font-size: 100px;
    vertical-align: middle;
}
</style>
