import Vue from 'vue'
import VueRouter from 'vue-router'
import SideBarHome from '@/components/SideBarHome'
import UserProfile from '@/components/User/UserProfile'
import Login from '@/components/Autentication/Login'
import Signin from '@/components/Autentication/Signin'
import Autentication from '@/components/Autentication/Autentication'
import NavBarHome from '@/components/Home/NavBarHome'
import Home from '@/components/Home/Home'
import Contact from '@/components/Home/Contact'
import About from '@/components/Home/About'
import Recomendation from '@/components/Recomendation/Recomendation'
import MealPlan from '@/components/MealPlan/MealPlan'
import SearchHealthyFood from '@/components/HealthyFood/SearchHealthyFood'

//import NutricionalHistory from '@/components/History/History'
import NutricionalHistory from '@/components/History/History'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'SideBarHome',
    component: SideBarHome,
    children: [
      {
        path: '/username',
        name: 'userProfile',
        component: UserProfile,
        props: true
      },
      {
        path: '/history',
        name: 'NutritionalHistory',
        component: NutricionalHistory,
        props: true
      },
      {
        path: '/mealplan',
        name: 'MealPlan',
        component: MealPlan,
        props: true
      },
      {
        path: '/recomendation',
        name: 'Recomendation',
        component: Recomendation,
        props: true
      },
      {
        path: '/search',
        name: 'SearchHealthyFood',
        component: SearchHealthyFood,
        props: true
      },
    ]
  },
  {
    path: '/autentication',
    name: 'autentication',
    component: Autentication,
    children: [
      {
        path: '/login',
        name: 'login',
        component: Login,
      },
      {
        path: '/signin',
        name: 'signin',
        component: Signin,
      },
    ]
  },
  
  {
    path: '/home',
    name: 'NavBarHome',
    component: NavBarHome,
    children: [
      {
        path: '/',
        name: 'Home',
        component: Home,
        props: true
      },
      {
        path: '/about',
        name: 'About',
        component: About,
        props: true
      },
      {
        path: '/contact',
        name: 'Contact',
        component: Contact,
        props: true
      },
    
    ]
  }
  
  
]

const router = new VueRouter({
  base: process.env.BASE_URL,
  routes
})

export default router
