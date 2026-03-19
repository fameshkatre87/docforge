import { ref } from 'vue'
import { useFilesStore } from '../stores/files'

export function useTool() {
  const store    = useFilesStore()
  const loading  = ref(false)
  const progress = ref(0)
  const error    = ref('')
  const resultUrl      = ref('')
  const resultFilename = ref('')

  async function process(endpoint, files, extraFields = {}) {
    error.value     = ''
    resultUrl.value = ''
    loading.value   = true
    progress.value  = 0

    const fd = new FormData()
    // Attach files — single or multiple
    if (Array.isArray(files) && files.length > 1) {
      files.forEach(f => fd.append('files', f))
    } else {
      const f = Array.isArray(files) ? files[0] : files
      fd.append('file', f)
    }
    // Extra fields (width, height, quality, etc.)
    Object.entries(extraFields).forEach(([k, v]) => fd.append(k, v))

    try {
      const blob = await store.uploadAndProcess(endpoint, fd, p => { progress.value = p })
      const url  = URL.createObjectURL(blob)
      resultUrl.value      = url
      resultFilename.value = extraFields._filename || 'result'
    } catch (e) {
      error.value = store.error || 'Something went wrong.'
    } finally {
      loading.value  = false
      progress.value = 0
    }
  }

  return { loading, progress, error, resultUrl, resultFilename, process }
}
