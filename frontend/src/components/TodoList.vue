<template>
  <div class="todo-list">
    <h1>My Todo List</h1>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <ul>
        <li v-for="todo in todos" :key="todo.id" class="todo-item">
          <h2>{{ todo.name }}</h2>
          <p>{{ todo.description }}</p>
          <p>Status: <strong>{{ todo.complete ? 'Completed' : 'Pending' }}</strong></p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'TodoList',
  setup() {
    const todos = ref([]);
    const loading = ref(false);

    onMounted(async () => {
      loading.value = true;
      try {
        const response = await axios.get('127.0.0.1:8000');
        todos.value = response.data;
      } catch (error) {
        console.error('Error fetching todo list:', error);
      } finally {
        loading.value = false;
      }
    });

    return { todos, loading };
  }
};
</script>

<style>
.todo-list {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.todo-item {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 10px;
}

.todo-item h2 {
  margin: 0 0 10px 0;
}

.todo-item p {
  margin: 0;
}
</style>
