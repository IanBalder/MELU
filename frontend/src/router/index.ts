import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ProfileView from "../views/ProfileView.vue";
import AccountHomeView from "../views/AccountHomeView.vue";
import BarMenuView from '@/views/BarMenuView.vue';

// Routes definition
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: LandingPage
  },
  {
    path: "/explore",
    name: "explore",
    component: AccountHomeView,
    meta: { requiresAuth: true }
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
    meta: { requiresAuth: true }
  },
  {
    path: '/barmenuview',
    name: 'barmenuview',
    component: BarMenuView,
    meta: { requiresAuth: true }
  }
]

// Router setup
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

import { jwtDecode } from "jwt-decode";

export  function isLoggedIn(): boolean {
  const token = localStorage.getItem("access_token");
  if (!token) return false;

  try {
    const decoded: { exp: number } = jwtDecode(token);
    const currentTime = Math.floor(Date.now() / 1000);
    return decoded.exp > currentTime;
  } catch (error) {
    console.error("Invalid token:", error);
    return false;
  }
}

// Router navigation guard
router.beforeEach((to, from, next) => {
  const loggedIn = isLoggedIn();
  console.log("Route:", to.path, "Logged In:", loggedIn);

  if (to.meta.requiresAuth && !loggedIn) {
    console.log("Redirecting to /login because user is not logged in.");
    next('/login');
  } else if (to.meta.guestOnly && loggedIn) {
    console.log("Redirecting to /explore because user is already logged in.");
    next('/explore');
  } else {
    console.log("Allowing navigation to:", to.path);
    next();
  }
});

export default router;
