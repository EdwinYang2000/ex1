import Vue from 'vue'
import App from './Message.vue'
import axios from 'axios'

window.http = axios

new Vue({
  el: '#app',
  render: h => h(App)
})
