<template>
  <div class="container">
    <article>
      <h1>{{ post.title }}</h1>
      <p>{{ post.body }}</p>
    </article>
    <aside>
      <h3>Posts you might be interested in</h3>
      <li v-for="relatedPost in relatedPosts" :key="relatedPost.id">
        <!-- <nuxt-link :to="{name: 'posts-id', params: {id: related.id}" -->
        <nuxt-link :to="`/posts/${relatedPost.id}`">{{ relatedPost.title }}</nuxt-link>
      </li>
    </aside>
  </div>
</template>

<script>
export default {
  //   async fetch({store }) {
  //   const response = await //store.dispatch
  // },
  async asyncData({ $axios, params }) {
    const response = await $axios.$get(
      `https://jsonplaceholder.typicode.com/posts/${params.id}`
    )
    return { post: response }
  },
  // asyncData() {
  //   return axios
  //     .get(`https://jsonplaceholder.typicode.com/posts/${this.id}`)
  //     .then((response) => {
  //       return { post: response.data }
  //     })
  // },
  data() {
    return {
      id: this.$route.params.id,
    }
  },

  computed: {
    // post() {
    //   return this.$store.state.posts.all.find((post) => post.id === this.id)
    // },
    relatedPosts() {
      return this.$store.state.posts.all.filter((post) => post.id !== this.id)
    },
  },
  // mounted() {
  //   fetch(`https://jsonplaceholder.typicode.com/posts/${this.id}`).then(
  //     (response) => {
  //       response.json().then((post) => {
  //         this.post = post
  //       })
  //     }
  //   )
  // },
  head() {
    return {
      title: this.post.title,
    }
  },
}
</script>

<style></style>
