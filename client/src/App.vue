<template>
    <div id='app'>
        <router-view />
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
</style>
