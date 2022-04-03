import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'



const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/liste',
    name: 'Films/Séries',

    component: () => import('../views/About.vue')
  },
  {
    path: '/recommandations',
    name: 'Recommandations',

    component: () => import('../views/Recommandations.vue')
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('../views/Contact.vue')
  },
  {
    path: '/connexion',
    name: 'Connexion',
    component: () => import('../views/Connexion.vue')
  },
  {
    path: '/profil',
    name: 'Profil',
    component: () => import('../views/Profil.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})


export default router
