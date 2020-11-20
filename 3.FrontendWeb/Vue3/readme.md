# Vue

## Installation
- Use VueCLI to scaffold projects quickly
  - npm install -g @vue/cli
- Install VueDevTools

## Application Instance
- Vue apps start at a single point
 ```const app = Vue.createApp({ /* options */ })```
- Register globals at app level
```
const app = Vue.createApp({})
app.component('SearchInput', SearchInputComponent)
app.directive('focus', FocusDirective)
app.use(LocalePlugin)
``` 
- After root component is made, it needs to be mounted
```
const vm = app.mount('#app')
```

## Component Instance
- Each component has the following options
  - methods
  - props
  - computed
  - inject
  - setup
- Also have lifecycle methods to hook into
  - mounted
  - updated
  - unmounted
  - created

### Life Cycle
- A parent component creates -> then processes childrens create/mount lifecycles - then parent mounts
  - This means you want to pass Props as early as created if your child HAS to have props for early initialization (like 3rd party API with DeckGL)

## Declarative Template Syntax
- Vue uses templates to render 
  - HTML Text: ```<span> Message: {{ msg }}</span>```
  - HTML Attributes: ```<div v-bind:id="dynamicId"></div>```
    - Shorthand: <a :href="url"> ... </a>
  - Directives: ```<p v-if="seen">Now you see me</p>```
  - Modifiers: ```<form v-on:submit.prevent="onSubmit">...</form>```
    - Shorthand ```<a @click="doSomething"> ... </a>```

## Data Option
- Needs to be a function, where you store reactive state
```
const app = Vue.createApp({
  data() {
    return { count: 4 }
  }
})

const vm = app.mount('#app')

console.log(vm.$data.count) // => 4
console.log(vm.count)       // => 4

// Assigning a value to vm.count will also update $data.count
vm.count = 5
console.log(vm.$data.count) // => 5

// ... and vice-versa
vm.$data.count = 6
console.log(vm.count) // => 
```

## Methods Option
- Methods to be accessed by a component. Don't use arrow functions cuz we need this to work.
```
const app = Vue.createApp({
  data() {
    return { count: 4 }
  },
  methods: {
    increment() {
      // `this` will refer to the component instance
      this.count++
    }
  }
})

const vm = app.mount('#app')

console.log(vm.count) // => 4

vm.increment()

console.log(vm.count) // => 5
```
### Debounce example
```
app.component('save-button', {
  created() {
    // Debouncing with Lodash
    this.debouncedClick = _.debounce(this.click, 500)
  },
  unmounted() {
    // Cancel the timer when the component is removed
    this.debouncedClick.cancel()
  },
  methods: {
    click() {
      // ... respond to click ...
    }
  },
  template: `
    <button @click="debouncedClick">
      Save
    </button>
  `
})
```
## Computed Options
- Allow us to remove logic from templates and keep in reactive methods.
- computed properties are cached based on their reactive dependencies.
```
Vue.createApp({
  data() {
    return {
      author: {
        name: 'John Doe',
        books: [
          'Vue 2 - Advanced Guide',
          'Vue 3 - Basic Guide',
          'Vue 4 - The Mystery'
        ]
      }
    }
  },
  computed: {
    // a computed getter
    publishedBooksMessage() {
      // `this` points to the vm instance
      return this.author.books.length > 0 ? 'Yes' : 'No'
    }
  }
}).mount('#computed-basics')
```
- Can do Getter/Setter Computed Prop
```
computed: {
  fullName: {
    // getter
    get() {
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set(newValue) {
      const names = newValue.split(' ')
      this.firstName = names[0]
      this.lastName = names[names.length - 1]
    }
  }
}
```
## Watcher Options
- Set up custom computed watchers/reactive props.
```
    watch: {
      // whenever question changes, this function will run
      question(newQuestion, oldQuestion) {
        if (newQuestion.indexOf('?') > -1) {
          this.getAnswer()
        }
      }
    },
```

## Classes/Style Bindings
- We bind to the class
```
<div
  class="static"
  :class="{ active: isActive, 'text-danger': hasError }"
></div>
```
- Can do in computed prop as well
```
<div :class="classObject"></div>
data() {
  return {
    isActive: true,
    error: null
  }
},
computed: {
  classObject() {
    return {
      active: this.isActive && !this.error,
      'text-danger': this.error && this.error.type === 'fatal'
    }
  }
}
```
- Can bind inline styles as well
```
<div :style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```

## Conditional Renderin
- Ways to programatically render templates
  - v-if
  - v-else
  - v-else-if
  - v-show

## List Rendering
- Ways to programmatically loop and render templates
  - v-for ```<li v-for="item in items">```
  - v-for with index ```<li v-for="(item, index) in items">```
  - v-for with object ```  <li v-for="value in myObject">```
  - v-for with key ```<div v-for="item in items" :key="item.id">```
    -  track each node's identity, and thus reuse and reorder existing elements

### Mutating Array
- All your standard array methods mutate an array and trigger state (pop, push, etc)
- Filter/Concat/Slice return a new array so you need to assign to the old array in memory
  - ```example1.items = example1.items.filter(item => item.message.match(/Foo/))```

## Event Handling
- Use v-on or @
``` <button @click="counter += 1">Add 1</button>```
- Can pass method to handler
- Can have separate handlers
```<button @click="one($event), two($event)">```
- Can use modifiers.
  - .stop
  - .prevent
  - .capture.
  - .self
  - .once
  - .passive
- Can use key modifiers.
  - ```<input @keyup.enter="submit" />```
  - ```<input @keyup.page-down="onPageDown" />```
  - ```<input @keyup.alt.enter="clear" />```

## Form Value Bindings
- use v-model
  - Creates two way data binding
```
<span>Multiline message is:</span>
<p style="white-space: pre-line;">{{ message }}</p>
<br />
<textarea v-model="message" placeholder="add multiple lines"></textarea
```

## Components
- Components are reusable elements with their own local properties
```
// Create a Vue application
const app = Vue.createApp({})

// Define a new global component called button-counter
app.component('button-counter', {
  data() {
    return {
      count: 0
    }
  },
  template: `
    <button @click="count++">
      You clicked me {{ count }} times.
    </button>`
})
```

- You can pass props to components
```
const app = Vue.createApp({})

app.component('blog-post', {
  props: ['title'],
  template: `<h4>{{ title }}</h4>`
})

app.mount('#blog-post-demo')

<div id="blog-post-demo" class="demo">
  <blog-post title="My journey with Vue"></blog-post>
  <blog-post title="Blogging with Vue"></blog-post>
  <blog-post title="Why Vue is so fun"></blog-post>
</div>
```
### Custom Events
- These can help us pass events from child component up 
```
<blog-post ... @enlarge-text="postFontSize += 0.1"></blog-post>
...
<button @click="$emit('enlarge-text')">
  Enlarge text
</button>
```

## Component Registration
- Can register components locally as well for webpack advantages
```
import ComponentA from './ComponentA'
import ComponentC from './ComponentC'

export default {
  components: {
    ComponentA,
    ComponentC
  }
  // ...
}
```
## Slots
- Mirrors web component spec for content distribution
```
<todo-button>
  Add todo
</todo-button>
```
```
<!-- todo-button component template -->
<button class="btn-primary">
  <slot></slot>
</button>
```
- Slots can contain other components or standard HTML
- Has access to same scope as the element
- Can used named slots
```
<div class="container">
  <header>
    <slot name="header"></slot>
  </header>
  <main>
    <slot></slot>
  </main>
  <footer>
    <slot name="footer"></slot>
  </footer>
</div>
```
```
<base-layout>
  <template v-slot:header>
    <h1>Here might be a page title</h1>
  </template>

  <template v-slot:default>
    <p>A paragraph for the main content.</p>
    <p>And another one.</p>
  </template>

  <template v-slot:footer>
    <p>Here's some contact info</p>
  </template>
</base-layout>
```
## Provide/Inject
- Way for us to avoid passing props down large trees or up trees
```
  provide: {
    user: 'John Doe'
  },
```
```
  inject: ['user'],
```
- To pass instance properties needs to be a function
```
  provide() {
    return {
      todoLength: this.todos.length
    }
  },
```
- To pass reactive props need to utilize composition API computed reactivity
```
  provide() {
    return {
      todoLength: Vue.computed(() => this.todos.length)
    }
  }
```

## Refs
- Can also add refs to elements to access them for manipulation
```
<input ref="input" />
 this.$refs.input.focus()
 ```

## Vue Reactivity
- Declare Reactive State
```
import { reactive } from 'vue'

// reactive state
const state = reactive({
  count: 0
})
```
- Can create standalone reactive values
```
import { ref } from 'vue'

const count = ref(0)
console.log(count.value) // 0

count.value++
console.log(count.value) // 1
```
- Don't need to unwrap refs in template
```
<template>
  <div>
    <span>{{ count }}</span>
    <button @click="count ++">Increment count</button>
  </div>
</template>

<script>
  import { ref } from 'vue'
  export default {
    setup() {
      const count = ref(0)
      return {
        count
      }
    }
  }
</script>
```
- To desctructure use toRefs
```
import { reactive, toRefs } from 'vue'

const book = reactive({
  author: 'Vue Team',
  year: '2020',
  title: 'Vue 3 Guide',
  description: 'You are reading this book right now ;)',
  price: 'free'
})

let { author, title } = toRefs(book)

title.value = 'Vue 3 Detailed Guide' // we need to use .value as title is a ref now
console.log(book.title) // 'Vue 3 Detailed Guide'
```
- Can declare computed properties
```
const count = ref(1)
const plusOne = computed(() => count.value + 1)

console.log(plusOne.value) // 2

plusOne.value++ // error
```
- Can use getters/setters on those computed properties
```
const count = ref(1)
const plusOne = computed({
  get: () => count.value + 1,
  set: val => {
    count.value = val - 1
  }
})

plusOne.value = 1
console.log(count.value) // 0
```
- Can use watchEffect for new watchers
```
const count = ref(0)

watchEffect(() => console.log(count.value))
// -> logs 0

setTimeout(() => {
  count.value++
  // -> logs 1
}, 100)
```
- Watch is still cleanest/lazyiest
```
// watching a getter
const state = reactive({ count: 0 })
watch(
  () => state.count,
  (count, prevCount) => {
    /* ... */
  }
)

// directly watching a ref
const count = ref(0)
watch(count, (count, prevCount) => {
  /* ... */
})
```
## Composition API
- Organization with Options suck, Long live composition
- First start with a setup method which takes Props/Context
```
<!-- MyBook.vue -->
<template>
  <div>{{ collectionName }}: {{ readersNumber }} {{ book.title }}</div>
</template>

<script>
  import { ref, reactive } from 'vue'

  export default {
    props: {
      collectionName: String
    },
    setup(props) {
      const readersNumber = ref(0)
      const book = reactive({ title: 'Vue 3 Guide' })

      // expose to template
      return {
        readersNumber,
        book
      }
    }
  }
</script>
```
- In setup we can setup lifecycle hooks with callbacks
  - https://v3.vuejs.org/guide/composition-api-lifecycle-hooks.html

## Vue Router
- install vuerouter
- basic setup is the following
```
const routes = [
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar }
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = new VueRouter({
  routes // short for `routes: routes`
})

// 4. Create and mount the root instance.
// Make sure to inject the router with the router option to make the
// whole app router-aware.
const app = new Vue({
  router
}).$mount('#app')
```
- Can utilize dynamic routes
```
  routes: [
    // dynamic segments start with a colon
    { path: '/user/:id', component: User }
  ]
```
```
const User = {
  template: '<div>User {{ $route.params.id }}</div>'
}
```
- Can utilize nested routes
```
const User = {
  template: `
    <div class="user">
      <h2>User {{ $route.params.id }}</h2>
      <router-view></router-view>
    </div>
  `
}
```
```
const router = new VueRouter({
  routes: [
    { path: '/user/:id', component: User,
      children: [
        {
          // UserProfile will be rendered inside User's <router-view>
          // when /user/:id/profile is matched
          path: 'profile',
          component: UserProfile
        },
        {
          // UserPosts will be rendered inside User's <router-view>
          // when /user/:id/posts is matched
          path: 'posts',
          component: UserPosts
        }
      ]
    }
  ]
})
```
- Can programitcally navigate
```
// literal string path
router.push('home')

// object
router.push({ path: 'home' })

// named route
router.push({ name: 'user', params: { userId: '123' } })

// with query, resulting in /register?plan=private
router.push({ path: 'register', query: { plan: 'private' } })
```
- Can use named routes
```
const router = new VueRouter({
  routes: [
    {
      path: '/user/:userId',
      name: 'user',
      component: User
    }
  ]
})
```
```
<router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>
router.push({ name: 'user', params: { userId: 123 }})
```

## Vuex
