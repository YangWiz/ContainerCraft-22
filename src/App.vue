<script setup>
import HelloWorld from './components/HelloWorld.vue'
import ToDoList from "@/components/ToDoList.vue"
</script>

<template>
  <header>
<!--    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />-->
    <div class="logo">
      <v-icon size="125">mdi-checkbox-marked-circle-auto-outline</v-icon>
    </div>
    <div class="wrapper">
      <HelloWorld msg="To Do List" />
    </div>
  </header>

  <main>
    <ToDoList />
<!--    <TheWelcome />-->
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
