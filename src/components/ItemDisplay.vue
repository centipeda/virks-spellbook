<template>
    <div class="item-display w-100">
        <Item v-for="spell in shown_spells" :spell="spell" :key="spell.title"></Item>
    </div>
</template>

<script>
import sp from '../assets/spells.json'
import Item from './Item.vue'

export default {
    name: 'ItemDisplay',
    components: {
        Item
    },
    props: ['query'],
    data: function() {
        return {
            spells: sp
        }
    },
    mounted: function() {
    },
    computed: {
        shown_spells() {
            if(this.query.length > 0) {
                const self = this;
                return this.spells.filter(function(s) {
                    return self.query.toLowerCase().split(" ").reduce((lastWordHit, q) => 
                        lastWordHit && (
                        s.title.toLowerCase().includes(q) ||
                        s.cast_time.toLowerCase().includes(q) ||
                        s.range.toLowerCase().includes(q) ||
                        s.level.toLowerCase().includes(q) ||
                        s.school.toLowerCase().includes(q) ||
                        s.spell_lists.reduce((prev, curr) => prev || curr.toLowerCase().includes(q), false) ||
                        s.description.reduce((prev, curr) => prev || curr.toLowerCase().includes(q), false) ||
                        s.duration.toLowerCase().includes(q)), true)
                })
            } else {
                return []
            }
        }
    }
}
</script>

<style>

</style>