import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ProfileView from "../views/ProfileView.vue";
import BarMenuView from "../views/BarMenuView.vue";
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: LandingPage
  },
  {
    path: '/about',
    name: 'about',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/barmenuview',
    name: 'barmenuview',
    component: BarMenuView,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Navigation guard to check authentication
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (!localStorage.getItem('access_token')) {
      next('/login');
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
