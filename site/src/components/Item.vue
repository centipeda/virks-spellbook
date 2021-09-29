<template>
<div class="item w-100 cf pa2 mt1">
    <div v-if="opened" class="fl tc toggler .v-mid" @click="opened = !opened"><strong>-</strong></div>
    <div v-else class="fl tc toggler .v-mid" @click="opened = !opened"><strong>+</strong></div>
    <div class="w-30 fl spell tl"><strong>{{ spell.title }}</strong></div>
    <div class="w-40 fr spell tr">{{ spell.type }}</div>
    <div v-if="opened" class="w-100 fl">
        <hr>
        <p class="tl ma0 detail"><strong>Casting Time: </strong>{{ spell.cast_time }}</p>
        <p class="tl ma0 detail"><strong>Range: </strong>{{ spell.range }}</p>
        <p class="tl ma0 detail"><strong>Components: </strong>{{ spell.components }}</p>
        <p class="tl ma0 detail"><strong>Duration: </strong>{{ spell.duration }}</p>
        <p class="tl ma0 detail"><strong>Spell Lists: </strong>{{ spell.spell_lists.join(", ") }}</p>
        <div v-for="d in spell.description" :key="d">
            <br>
            <p class="tl ma0 detail">{{ d }}</p>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'Item',
    props: ['spell'],
    data: function() {
        return {
            opened: false
        }
    }
}
</script>

<style>
.item {
    border-width: 2px;
    border-style: solid;
    border-color: black;
}
.spell {
    font-family: 'MrsEavesSmallCaps';
    font-size: 14pt;
}
.detail {
    font-size: 12pt;
    font-family: 'ScalaSansRegular';
}
.toggler {
    width: 5%;
    height: 100%;
    padding: 0;
    margin: 0;
}
</style>