module.exports = {
    devServer: {
        proxy: {
            '^/api': {
                target: 'https://localhost:5000/'
            },
            '^/login': {
                target: 'https://localhost:5000/'
            },
            '^/oauth2callback': {
                target: 'https://localhost:5000/'
            }
        }
    }
}
