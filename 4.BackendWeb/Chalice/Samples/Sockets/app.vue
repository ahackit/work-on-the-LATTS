<template>
  <div>
    <p v-if="isConnected">We're connected to the server!</p>
    <p>Message from server: "{{socketMessage}}"</p>
    <button @click="pingServer()">Ping Server</button>
  </div>
</template>

<script>
import Sockette from "sockette";

export default {
  name: 'App',
  data() {
    return {
      isConnected: false,
      socketMessage: '',
      ws: {}
    }
  },

  sockets: {

  },

  methods: {
    pingServer() {
      // Send the "pingServer" event to the server.
      this.$socket.emit('pingServer', 'PING!')
    },
    connect() {
      // Fired when the socket connects.
      this.isConnected = true;
    },

    disconnect() {
      this.isConnected = false;
    },

    // Fired when the server sends something on the "messageChannel" channel.
    messageChannel(data) {
      this.socketMessage = data
    }
  },
  mounted(){
    this.ws = new Sockette(
          "wss://amazonaws.com/api/",
          {
            timeout: 5e3,
            maxAttempts: 1,
            onopen: () => this.connect(),
            onmessage: (e) => this.messageChannel(e.data),
            onreconnect: e => console.log("Reconnecting...", e),
            onmaximum: e => console.log("Stop Attempting!", e),
            onclose: e => console.log("Closed!", e),
            onerror: e => console.log("Error:", e)
          }
        );

  }
}
</script>