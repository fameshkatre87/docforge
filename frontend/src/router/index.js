import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../views/LandingPage.vue'),
  },
  {
    path: '/login',
    component: () => import('../views/LoginView.vue'),
  },
  {
    path: '/register',
    component: () => import('../views/RegisterView.vue'),
  },
  {
    path: '/dashboard',
    component: () => import('../views/DashboardView.vue'),
  },
  {
    path: '/tools/pdf-merge',
    component: () => import('../views/tools/PdfMergeView.vue'),
  },
  {
    path: '/tools/pdf-split',
    component: () => import('../views/tools/PdfSplitView.vue'),
  },
  {
    path: '/tools/pdf-compress',
    component: () => import('../views/tools/PdfCompressView.vue'),
  },
  {
    path: '/tools/word-to-pdf',
    component: () => import('../views/tools/WordToPdfView.vue'),
  },
  {
    path: '/tools/pdf-to-word',
    component: () => import('../views/tools/PdfToWordView.vue'),
  },
  {
    path: '/tools/image-resize',
    component: () => import('../views/tools/ImageResizeView.vue'),
  },
  {
    path: '/tools/image-compress',
    component: () => import('../views/tools/ImageCompressView.vue'),
  },
  {
    path: '/tools/images-to-pdf',
    component: () => import('../views/tools/ImagesToPdfView.vue'),
  },
  {
    path: '/tools/remove-pages',
    component: () => import('../views/tools/RemovePagesView.vue'),
  },
  {
    path: '/admin',
    component: () => import('../views/AdminView.vue'),
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/',
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior: () => ({ top: 0 }),
})

export default router