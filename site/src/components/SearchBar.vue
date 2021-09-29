<template>
    <div class="w-100">
        <h2 class="search ma2 normal">Search for a spell...</h2>
        <input class="search" id="search-text" type="text" placeholder="ex. ranger 1st-level conjuration"
        @input="$emit('update:query', $event.target.value)" :value="query">
    </div>
    <a class="w-100" @click="getSpellCards" :href="'/spellcard?cards='+ selection.join(',')">Get Spell Cards: {{ selection }}</a>
</template>

<script>
export default {
    name: 'SearchBar',
    props: {
        query: String,
        selection: Array
    },
    emits: ['update:query'],
    methods: {
        search() {
            console.log(this.query)
        },
        getSpellCards() {
            if(this.selection.length > 0) {
                console.log(this.selection)
            }
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