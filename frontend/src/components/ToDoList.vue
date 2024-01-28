<script>
export default {
  name: "ToDoList",
  data: () => ({
    todos: [],
    mockTodos: [
      {}
    ],
    enableMultiSelect: false,
    action: '', // can only be ADD or EDIT
    ADD: 'Add',
    EDIT: 'Edit',
    editedItem: {},
    showMenu: false,
    showDelConfirm: false,
    showSnackbar: false,
    showEditDialog: false,
    snackbarText: '',
    
  mounted() {
    this.todos = []
    this.todos = this.mockTodos
    this.fetchTodos()
  },
  watch: {
    todos(newVal, oldVal) {
      // add prop "selected" to the new items
      let newItems = newVal.filter(item => !oldVal.includes(item))
      newItems.forEach(item => {
        item.selected = false
      })
    },
  },
  computed: {
  },
  methods: {
    fetchTodos() {
      this.axios.get('/list')
          .then(response => {
            this.todos = response.data
          })
          .catch(error => {
            this.notify('Error fetching todos')
          })
    },
    notify(msg) {
      this.snackbarText = msg
      this.showSnackbar = true
    },
    getSelectedItems() { // not in computed because it doesn't need to be reactive
      const selectedItems = this.todos.filter(item => item.selected)
      return selectedItems
    },
    showEdit(item) { 
      this.action = item.id ? this.EDIT : this.ADD
      this.editedItem = {...item}
      this.showEditDialog = true
    },
    updateItem(item) {
      const body = {
        id: item.id,
        name: item.name,
        description: item.description,
        complete: item.done,
      }
      this.axios.put('/list', body)
          .then(response => {
            this.notify('Item updated')
            this.fetchTodos()
          })
          .catch(error => {
            this.notify('Error updating item')
            // for offline testing, update the local todos
            const index = this.todos.findIndex(todo => todo.id === item.id)
            this.todos[index] = item
          })
      this.showEditDialog = false 
    },
    addItem(item) {
      const body = {
        name: item.name,
        description: item.description,
        complete: item.done,
      }
      this.axios.post('/list', body)
          .then(response => {
            this.notify('Item added')
            this.fetchTodos()
          })
          .catch(error => {
            this.notify('Error adding item')
            // for offline testing
            item.id = this.todos.length + 1
            this.todos.push(item)
          })
      this.showEditDialog = false
    },
    _delItem(id) { // only used internally
      this.axios.delete('/list/' + id)
          .then(response => {
            this.notify('Item deleted')
          })
          .catch(error => {
            this.notify('Error deleting item')
          })
    },
    delItems() {
      const items = this.getSelectedItems() 
      items.forEach(item => {
        this._delItem(item.id)
      })
      this.todos = this.todos.filter(item => !items.includes(item)) // for offline testing
      this.fetchTodos()
      this.showDelConfirm = false
    },
    checkItem(item) {
      item.done = !item.done
      //TODO: call api
    },
    toggleMultiSelect() {
      this.enableMultiSelect = !this.enableMultiSelect
      this.showMenu = false
    },
  }
}
</script>

<template>
  <v-card
      class="mx-auto"
      max-width="600"
  >
    <v-toolbar color="secondary">
      <v-btn variant="text" icon="mdi-menu"
             id="menu-activator"
      ></v-btn>
      <v-menu
          activator="#menu-activator"
          v-model="showMenu"
          :close-on-content-click="false"
          :nudge-width="200"
          offset-y
      >
<!--        multi select btn -->
        <v-list>
          <v-list-item @click="toggleMultiSelect()">
            <v-list-item-title> 
              <v-icon>mdi-checkbox-multiple-marked-outline</v-icon>
              {{ enableMultiSelect ? 'Disable' : '' }}
              Multi Select
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-toolbar-title>To Do List</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn variant="text" icon="mdi-magnify"></v-btn>
<!--      TODO: search-->

      <v-dialog v-model="showDelConfirm"
                width="auto"
      >
        <v-card>
          <v-card-text>Are you sure you want to delete the selected item(s)?</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                color="red"
                @click="showDelConfirm = false"
            >
              Cancel
            </v-btn>
            <v-btn
                color="green"
                @click="delItems()"
            >
              OK
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      
      <v-btn icon="mdi-plus"
             @click="showEdit({id : null, name: '', description: '', done: false})"
      ></v-btn>
<!--      reusing the same dialog for add and edit-->
    </v-toolbar>

    <v-dialog v-model="showEditDialog"
                    width="30%"
    >
      <v-card>
        <v-card-title>{{ action }} Item</v-card-title>
        <v-card-text>
          <v-text-field label="Name"
                        v-model="editedItem.name"
          ></v-text-field>
          <v-text-field label="Description"
                        v-model="editedItem.description"
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="red"
              @click="showEditDialog = false"
          >
            Cancel
          </v-btn>
          <v-btn
              color="green"
              @click="action === ADD ? addItem(editedItem) : updateItem(editedItem)"
          >
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-list lines="two">
      <v-list-item
          v-for="todo in todos"
          :key="todo.id"
          :title="todo.name"
          :subtitle="todo.description"
      >
        <template v-slot:prepend="{ isActive }">
          <v-list-item-action start>
<!--        multi-select or mark as complete-->
            <v-checkbox-btn :model-value="isActive" 
                            v-model="todo.selected"
                            v-if="enableMultiSelect"
            ></v-checkbox-btn>
            <v-btn :model-value="todo.done"
                   @click="checkItem(todo)"
                   :icon="todo.done ? 'mdi-check-circle' : 'mdi-circle-outline'"
                   variant="text"
                   v-else
            ></v-btn>
          </v-list-item-action>
        </template>
        <template v-slot:append>
          <v-btn
              icon="mdi-pencil"
              @click="showEdit(todo)"
          ></v-btn>
          
        </template>
      </v-list-item>
      
<!--      notification snackbar for all actions-->
      <v-snackbar
          v-model="showSnackbar"
      >
        {{ snackbarText }}
        <template v-slot:actions>
          <v-btn
              color="pink"
              variant="text"
              @click="showSnackbar = false"
          >
            Close
          </v-btn>
        </template>
      </v-snackbar>
      
<!--      only show this toolbar when in multi select mode -->
      <div>
        <v-toolbar v-if="enableMultiSelect"
                   width="50%">
          <v-btn icon="mdi-delete"
                 @click="showDelConfirm = true"
          ></v-btn>
          <!--      TODO: multi check-->
<!--          TODO: center btns-->


          <v-spacer></v-spacer>

          <v-btn icon="mdi-check"
                 @click="toggleMultiSelect()"
          ></v-btn>
        </v-toolbar>
      </div>
    </v-list>
    
  </v-card>
</template>

<style scoped>

</style>
