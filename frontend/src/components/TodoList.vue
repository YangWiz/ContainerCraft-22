<template>
  <div class="todo-list">
    <h1 class="header">My Todo List</h1>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else class="todo-container">
      <ul class="todo-items">
        <li v-for="todo in todos" :key="todo.id" class="todo-item">
          <div class="item-header">
            <h2>{{ todo.name }}</h2>
            <span class="status" :class="{ 'completed': todo.complete }">{{ todo.complete ? 'Completed' : 'Pending' }}</span>
            <!-- Toggle Button -->
            <button @click="toggleComplete(todo)">
              {{ todo.complete ? 'Mark as Incomplete' : 'Mark as Complete' }}
            </button>
          </div>
          <p>{{ todo.description }}</p>
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
        const response = await axios.get('http://localhost:8000/list');
        todos.value = response.data;
      } catch (error) {
        console.error('Error fetching todo list:', error);
      } finally {
        loading.value = false;
      }
    });

    // Method to toggle the completion status
    const toggleComplete = async (todo) => {
      try {
        const apiPath = todo.complete ? `list/incomplete/${todo.id}` : `list/complete/${todo.id}`;
        await axios.put(`http://localhost:8000/${apiPath}`);

        // Optimistically update the UI
        todo.complete = !todo.complete;
      } catch (error) {
        console.error('Error updating task status:', error);
        // Optionally revert the UI change or inform the user
      }
    };

    return { todos, loading, toggleComplete };
  }
};
</script>
