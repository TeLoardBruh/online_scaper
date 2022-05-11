<template>
  <component :is="layout">
    <slot />
  </component>
</template>

<script lang="ts">
const defaultLayout = 'AppLayoutDefault'
export default {
  name: "AppLayout",
  computed: {
    layout(this: any): any {
    
      const layout: any = this.$route.meta.layout || defaultLayout
      return () => import(`@/layouts/${layout}.vue`)
    }
  }
}
</script>
© 2022 GitHub, Inc.
Terms
