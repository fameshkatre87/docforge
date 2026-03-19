import { defineStore } from 'pinia'
import api from '../api/axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user') || 'null'),
    token: localStorage.getItem('access_token') || null,
  }),

  getters: {
    isLoggedIn: state => !!state.token,
    isAdmin:    state => state.user?.is_staff === true,
    userName:   state => state.user?.username || state.user?.email || 'User',
    userPlan:   state => state.user?.plan || 'free',
  },

  actions: {
    async login(email, password) {
      const { data } = await api.post('/auth/login/', { email, password })
      this.token = data.access
      this.user  = data.user
      localStorage.setItem('access_token',  data.access)
      localStorage.setItem('refresh_token', data.refresh)
      localStorage.setItem('user', JSON.stringify(data.user))
    },

    async register(username, email, password) {
      await api.post('/auth/register/', { username, email, password })
    },

    async fetchProfile() {
      const { data } = await api.get('/auth/me/')
      this.user = data
      localStorage.setItem('user', JSON.stringify(data))
    },

    logout() {
      this.token = null
      this.user  = null
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user')
    },
  },
})
