import { defineStore } from 'pinia'
import api from '../api/axios'

export const useFilesStore = defineStore('files', {
  state: () => ({
    pdfHistory:   [],
    imageHistory: [],
    loading: false,
    error: null,
  }),

  actions: {
    async fetchPdfHistory() {
      const { data } = await api.get('/pdf/history/')
      this.pdfHistory = data
    },

    async fetchImageHistory() {
      const { data } = await api.get('/image/history/')
      this.imageHistory = data
    },

    // Generic file-upload helper — returns a blob URL for download
    async uploadAndProcess(endpoint, formData, onProgress) {
      this.loading = true
      this.error   = null
      try {
        const { data } = await api.post(endpoint, formData, {
          responseType: 'blob',
          headers: { 'Content-Type': 'multipart/form-data' },
          onUploadProgress: e => {
            if (onProgress && e.total)
              onProgress(Math.round((e.loaded * 100) / e.total))
          },
        })
        return data   // Blob
      } catch (err) {
        this.error = err.response?.data?.error || 'Something went wrong.'
        throw err
      } finally {
        this.loading = false
      }
    },
  },
})
