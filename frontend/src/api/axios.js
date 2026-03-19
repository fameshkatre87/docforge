// import axios from 'axios'

// const api = axios.create({
//   baseURL: '/api',
//   timeout: 60000, // 60s for large file uploads
// })

// // Attach JWT token to every request
// api.interceptors.request.use(config => {
//   const token = localStorage.getItem('access_token')
//   if (token) config.headers.Authorization = `Bearer ${token}`
//   return config
// })

// // Auto-refresh on 401
// api.interceptors.response.use(
//   res => res,
//   async err => {
//     const original = err.config
//     if (err.response?.status === 401 && !original._retry) {
//       original._retry = true
//       const refresh = localStorage.getItem('refresh_token')
//       if (refresh) {
//         try {
//           const { data } = await axios.post('/api/auth/refresh/', { refresh })
//           localStorage.setItem('access_token', data.access)
//           original.headers.Authorization = `Bearer ${data.access}`
//           return api(original)
//         } catch {
//           localStorage.clear()
//           window.location.href = '/login'
//         }
//       } else {
//         localStorage.clear()
//         window.location.href = '/login'
//       }
//     }
//     return Promise.reject(err)
//   }
// )

// export default api

import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 60000,
})

// Attach JWT token if available (optional)
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// Remove redirect on 401 — tools work without login
api.interceptors.response.use(
  res => res,
  async err => {
    const original = err.config
    if (err.response?.status === 401 && !original._retry) {
      original._retry = true
      const refresh = localStorage.getItem('refresh_token')
      if (refresh) {
        try {
          const { data } = await axios.post('/api/auth/refresh/', { refresh })
          localStorage.setItem('access_token', data.access)
          original.headers.Authorization = `Bearer ${data.access}`
          return api(original)
        } catch {
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
          localStorage.removeItem('user')
          // No redirect — just reject
        }
      }
    }
    return Promise.reject(err)
  }
)

export default api