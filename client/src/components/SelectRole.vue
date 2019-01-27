<template>
    <div class='main'>
        <div class='icon'><i class='fas fa-gavel fa-10x'></i></div>
        <p class='icon-text'>OR</p>
        <div class='icon'><i class='fas fa-cookie-bite fa-10x'></i></div>
    </div>
</template>

<style scoped>
@import 'https://use.fontawesome.com/releases/v5.6.3/css/all.css';

.icon {
    color: #1D69D3;
    padding: 10px;
    margin: 50px;
    border: solid 15px;
    border-radius: 10px;
    display: inline-block;
    filter: saturate(50%);
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
    transform: translateY(-80px);
}
</style>
