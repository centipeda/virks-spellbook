<template>
    <div class="item-display w-100">
        <Item v-for="spell in shown_spells" :initialSelect="selected_spells.includes(spell.id)" :spell="spell" :key="spell.title" @selected="selected" @unselected="unselected"></Item>
    </div>
</template>

<script>
import sp from '../../../data/spells.json'
import Item from './Item.vue'

export default {
    name: 'ItemDisplay',
    components: {
        Item
    },
    props: ['query'],
    data: function() {
        return {
            spells: sp,
            selected_spells: []
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
                        self.selected_spells.includes(s.id) ||
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
                return this.spells.filter(s => this.selected_spells.includes(s.id))
            }
        }
    },
    methods: {
        selected: function(id) {
            this.selected_spells.push(id)
            this.$emit('update:selected_spells', this.selected_spells)
        },
        unselected: function(id) {
            this.selected_spells.splice(this.selected_spells.indexOf(id), 1)
            this.$emit('update:selected_spells', this.selected_spells)
        }
    }
}
</script>

<style>

</style>