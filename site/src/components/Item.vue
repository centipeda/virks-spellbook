<template>
<div class="item w-100 cf mt1" v-bind:class="[selected ? 'selected' : '']">
    <div v-if="opened" class="fl tc toggler v-mid" @click="opened = !opened"><strong>-</strong></div>
    <div v-else class="fl tc toggler v-mid" @click="opened = !opened"><strong>+</strong></div>
    <div class="w-30 fl spell pt2 pb2 tl"><strong>{{ spell.title }}</strong></div>
    <div class="fr cbox-holder" @click="select">
        <div class="cbox" v-bind:class="[selected ? 'cbox-checked' : '']"></div>
    </div>
    <div class="w-40 fr spell pt2 pb2 tr">{{ spell.type }}</div>
    <div v-if="opened" class="w-100 fl pl3 pr3 pb3">
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
    props: ['spell', 'initialSelect'],
    data: function() {
        return {
            opened: false,
            selected: this.initialSelect
        }
    },
    methods: {
        select: function() {
            this.selected = !this.selected;
            if(this.selected)
                this.$emit('selected', this.spell.id)
            else
                this.$emit('unselected', this.spell.id)
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
    height: 36px;
    padding-top: 9px;
}
.cbox {
    height: 13px;
    width: 13px;
    border-width: 2px;
    border-style: solid;
    border-color: black;
    margin-left: auto;
    margin-right: auto;
    margin-top: 12.5px;
    background-color: white;
    margin-bottom: 10px;
    padding: 0;
}
.cbox-holder {
    width: 5%;
}
.selected {
    background-color: #add8e6;
}
.cbox-checked {
    background-color: #808080;
}
</style>