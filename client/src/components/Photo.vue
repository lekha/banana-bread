<template>
    <div class='main'>
        <label>File
            <input type='file' id='file' ref='file' v-on:change='handleFileUpload()'/>
        </label>
        <br>
        <button v-on:click='submitFile()'>Submit</button>
        <p v-if='fileUploaded'>File successfully uploaded!</p>
        <img v-if='imageUrl != null' v-bind:src='imageUrl' />
    </div>
</template>

<script>
export default {
    name: 'Photo',
    data() {
        return {
            file: '',
            fileUploaded: false,
            imageUrl: null
        }
    },
    created() {
        this.getCurrentFile();
    },
    methods: {
        handleFileUpload() {
            this.file = this.$refs.file.files[0]; 
        },
        submitFile() {
            let formData = new FormData();
            formData.append('file', this.file);
            this.$http.post('api/upload', formData, {
                headers: {
                    'Content-Type': 'multipart-form-data'
                }    
            }).then((response) => {
                this.fileUploaded = true;
                this.imageUrl = response.data.image_url;
            })
        },
        getCurrentFile() {
            this.$http.get('api/photo').then((response) => {
                this.imageUrl = response.data.image_url;
            })
        }
    },
}
</script>

<style>
label {
    padding: 7px;
    font-size: 40px;    
}

button {
    padding: 7px;
    font-size: 25px;
}
</style>
