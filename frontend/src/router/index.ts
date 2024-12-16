import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ProfileView from "../views/ProfileView.vue";
import AccountHomeView from "../views/AccountHomeView.vue";

function isLoggedIn(): boolean {
  const token = localStorage.getItem('jwt');
  return !!token;
}

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: LandingPage
  },
  {
    path: "/main",
    name: "AccountHomeView",
    component: AccountHomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: { guestOnly: true }
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
    meta: { guestOnly: true }
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
  },
  /*{
    path: '/barmenuview',
    name: 'barmenuview',
    component: BarMenuView,
  }*/
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Navigation guard to check authentication
router.beforeEach((to, from, next) => {
  const loggedIn = isLoggedIn();

  if (to.meta.requiresAuth && !loggedIn) {
    if (!localStorage.getItem('access_token')) {
      next('/login');
    } else if (to.meta.questionOnly && loggedIn) {
      next('/about');
    }
  } else {
    next();
  }
});

export default router;
