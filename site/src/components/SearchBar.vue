<template>
    <div class="w-100">
        <h2 class="search ma2 normal">Search for a spell...</h2>
        <input class="search" id="search-text" type="text" placeholder="ex. ranger 1st-level conjuration"
        @input="$emit('update:query', $event.target.value)" :value="query">
    </div>
    <a v-if="selection.length > 0" target="_blank" class="w-40 f5 link br-pill pv2 mt2 mb2 dib get-btn-active" @click="getSpellCards" :href="'/spellcard?cards='+ selection.join(',')">
        Get selected as printable spell cards
    </a>
    <a v-else class="w-40 f5 link br-pill pv2 mt2 mb2 dib get-btn" @click="getSpellCards" disabled="disabled">
        Get selected as printable spell cards
    </a>
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
    .get-btn {
        background-color: gray;
        color: black;
        font-family: 'ScalaSansRegular';
        cursor: not-allowed;
    }
    .get-btn-active {
        background-color: #add8e6;
        color: black;
        font-family: 'ScalaSansRegular';
    }
</style>