import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Contact from '../views/Contact.vue'
import Message from '../views/message-board-app/src/Message.vue'

Vue.use(Router)

const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/about',
        component: About
    },
    {
        path: '/contact',
        component: Contact
    },
    {
        path:'/message',
        component: Message
    },
]

export default new Router({
    mode: 'history',
    routes: routes
})