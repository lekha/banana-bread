<template>
    <div class='main'>
        <h1>Leaderboards</h1>
        <div class='leaderboard-wrapper' v-for='(ranking, category) in rankings' :key='category'>
            <h2>{{ category }}</h2>
            <div class='leaderboard'>
                <h3>Rank</h3>
                <h3>Baker</h3>
                <h3>Score</h3>
            </div>
            <div class='leaderboard' v-for='(rank, i) in ranking' :key='i'>
                <p>{{ i }}.</p>
                <p>{{ i }}</p>
                <p>{{  rank }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Leaderboard',
    data() {
        return {
            rankings: []
        }
    },
    created() {
        this.loadRankings();
    },
    methods: {
        loadRankings() {
            this.$http.get('api/rankings').then((response) => {
                this.rankings = response.data;
            })
        }
    }
}
</script>

<style scoped>
.main {
    margin-left: auto;
    margin-right: auto;
    width: 90%;
}

h1 {
    font-weight: normal;
}

h2 {
    font-weight: normal
}

.leaderboard {
    display: grid;
    grid-template-columns: 20px auto 30px;
    grid-template-rows: auto;
    align-items: center;
    justify-items: center;
}
</style>
