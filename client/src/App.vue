<template>
    <div id='app'>
        <transition name='router' mode='out-in'>
            <router-view />
        </transition>
    </div>
</template>

<style>
@import 'https://fonts.googleapis.com/css?family=Baloo+Thambi';

html {
    height: 100%;
    margin: 0;
    padding: 0;
}

body {
    background-color: #F8F8FC;
    font-family: 'Baloo Thambi', cursive;
    font-size: 2em;
    display: grid;
    justify-items: center;
    align-items: center;
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
}

#app {
    width: 100%;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
}

.router-enter-active, .router-leave-active {
    transition-duration: 0.3s;
    transition-property: opacity;
    transition-timing-function: ease;
}

.router-enter, .router-leave-active {
    opacity: 0;
}
</style>
