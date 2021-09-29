<template>
    <div class="search-bar w-100">
        <h2 class="search ma2 normal">Search for a spell...</h2>
        <input class="search" id="search-text" type="text" placeholder="ex. 1st-level conjuration ranger"
        @input="$emit('update:query', $event.target.value)" :value="query">
    </div>
</template>

<script>
export default {
    name: 'SearchBar',
    props: {
        query: String
    },
    emits: ['update:query'],
    methods: {
        search() {
            console.log(this.query)
        }
    }
}
</script>

<style>
    .search {
        height: 100%;
        font-size: 18pt;
        font-family: 'ScalaSansRegular';
    }
    #search-text {
        width: 75%;
    }
    #search-submit {
        width: 25%;
    }
</style>