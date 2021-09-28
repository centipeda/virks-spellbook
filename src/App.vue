<template>
  <h1 class="title">Virk's Spellbook</h1>
  <div class="fl w-25-ns pa2"></div>
    <div class="w-50 fl">
      <SearchBar v-model:query="query"/>
      <ItemDisplay :query="query"/>
    </div>
  <div class="fl w-25-ns pa2"></div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import ItemDisplay from './components/ItemDisplay.vue'

export default {
  name: 'App',
  components: {
    SearchBar,
    ItemDisplay
  },
  data: function() {
    return {
      query: ""
    }
  }
}
</script>

<style src="./../node_modules/tachyons/css/tachyons.min.css"></style>
<style>
@font-face {
    font-family: 'MrsEavesSmallCaps';
    src: url('assets/MrsEavesSmallCaps.woff2') format('woff2'),
        url('assets/MrsEavesSmallCaps.woff') format('woff');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}
@font-face {
  font-family: "ScalaSansRegular";
  src: url('assets/ScalaSans-Regular.otf') format("opentype");
}
h1.title {
  font-family: 'MrsEavesSmallCaps', sans-serif;
  font-size: 4em;
}
#app {
  font-family: sans-serif;
  text-align: center;
}
</style>
