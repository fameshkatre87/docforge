<template>
  <AppLayout>
    <div class="tool-card fade-up">
      <div class="card-header">
        <h1 class="card-title">Remove PDF Pages</h1>
        <p class="card-sub">Upload a PDF, select pages to remove, download cleaned PDF</p>
      </div>

      <!-- Upload Zone -->
      <div
        class="upload-zone"
        :class="{ dragging: isDragging }"
        @click="$refs.fileInput.click()"
        @dragover.prevent="isDragging = true"
        @dragleave="isDragging = false"
        @drop.prevent="onDrop"
      >
        <span class="upload-icon">📄</span>
        <p class="upload-title">Click or drag PDF here</p>
        <p class="upload-hint">We'll show you all pages to select which to remove</p>
        <input ref="fileInput" type="file" accept=".pdf" style="display:none" @change="onFileChange" />
      </div>

      <!-- File Info -->
      <div v-if="fileName" class="file-info">
        <span class="file-icon">📄</span>
        <span class="file-name">{{ fileName }}</span>
        <span v-if="totalPages" class="file-pages">{{ totalPages }} pages</span>
        <button class="remove-btn" @click="reset">×</button>
      </div>

      <!-- Page Selector -->
      <div v-if="totalPages" class="pages-section">
        <div class="pages-header">
          <p class="pages-label">Select pages to <strong>remove</strong>:</p>
          <div class="pages-actions">
            <button class="action-btn" @click="selectAll">Select All</button>
            <button class="action-btn" @click="clearAll">Clear</button>
          </div>
        </div>

        <div class="pages-grid">
          <button
            v-for="n in totalPages"
            :key="n"
            class="page-btn"
            :class="{ selected: selectedPages.includes(n) }"
            @click="togglePage(n)"
          >
            {{ n }}
          </button>
        </div>

        <p v-if="selectedPages.length" class="selected-info">
          {{ selectedPages.length }} page(s) will be removed →
          {{ totalPages - selectedPages.length }} page(s) will remain
        </p>
      </div>

      <!-- Loading Info -->
      <p v-if="loadingInfo" class="loading-text">⏳ Reading PDF...</p>

      <!-- Error -->
      <p v-if="error" class="error-msg">⚠ {{ error }}</p>

      <!-- Process Button -->
      <button
        class="process-btn"
        :disabled="!selectedPages.length || loading"
        @click="process"
      >
        <span v-if="loading" class="spinner"></span>
        <span v-else>🗑️ Remove Selected Pages</span>
      </button>

      <!-- Result -->
      <div v-if="resultUrl" class="result-box">
        <div class="result-icon">✅</div>
        <p class="result-text">Pages removed successfully!</p>
        <p class="result-sub">{{ totalPages - selectedPages.length }} pages remaining</p>
        <a :href="resultUrl" download="cleaned.pdf" class="download-btn">⬇ Download PDF</a>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import { ref } from 'vue'
import AppLayout from '../../components/AppLayout.vue'
import api from '../../api/axios'

const fileInput    = ref(null)
const fileName     = ref('')
const fileObj      = ref(null)
const totalPages   = ref(0)
const selectedPages = ref([])
const isDragging   = ref(false)
const loading      = ref(false)
const loadingInfo  = ref(false)
const error        = ref('')
const resultUrl    = ref('')

function onDrop(e) {
  isDragging.value = false
  const f = e.dataTransfer.files[0]
  if (f) loadFile(f)
}

function onFileChange(e) {
  const f = e.target.files[0]
  if (f) loadFile(f)
  e.target.value = ''
}

async function loadFile(f) {
  reset()
  fileObj.value  = f
  fileName.value = f.name
  loadingInfo.value = true
  error.value = ''

  try {
    const fd = new FormData()
    fd.append('file', f)
    const { data } = await api.post('/pdf/info/', fd)
    totalPages.value = data.total_pages
  } catch {
    error.value = 'Could not read PDF. Please try another file.'
  } finally {
    loadingInfo.value = false
  }
}

function togglePage(n) {
  const idx = selectedPages.value.indexOf(n)
  if (idx === -1) selectedPages.value.push(n)
  else selectedPages.value.splice(idx, 1)
}

function selectAll() {
  selectedPages.value = Array.from({ length: totalPages.value }, (_, i) => i + 1)
}

function clearAll() {
  selectedPages.value = []
}

function reset() {
  fileName.value     = ''
  fileObj.value      = null
  totalPages.value   = 0
  selectedPages.value = []
  resultUrl.value    = ''
  error.value        = ''
}

async function process() {
  if (!fileObj.value || !selectedPages.value.length) return
  loading.value = true
  error.value   = ''
  resultUrl.value = ''

  try {
    const fd = new FormData()
    fd.append('file', fileObj.value)
    fd.append('pages', selectedPages.value.join(','))

    const { data } = await api.post('/pdf/remove-pages/', fd, { responseType: 'blob' })
    resultUrl.value = URL.createObjectURL(data)
  } catch {
    error.value = 'Something went wrong. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.tool-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 20px; padding: 36px; max-width: 680px;
}
.card-header  { margin-bottom: 28px; }
.card-title   { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 26px; }
.card-sub     { color: var(--muted); font-size: 14px; margin-top: 6px; }

.upload-zone {
  border: 2px dashed var(--border); border-radius: 13px;
  padding: 40px 24px; text-align: center; cursor: pointer;
  transition: all 0.2s; margin-bottom: 20px;
}
.upload-zone:hover, .upload-zone.dragging {
  border-color: var(--accent); background: #ff6b3508;
}
.upload-icon  { font-size: 40px; display: block; margin-bottom: 12px; }
.upload-title { font-size: 15px; font-weight: 500; }
.upload-hint  { color: var(--muted); font-size: 13px; margin-top: 6px; }

.file-info {
  display: flex; align-items: center; gap: 10px;
  background: var(--surface2); border-radius: 9px;
  padding: 11px 14px; margin-bottom: 20px; font-size: 13.5px;
}
.file-icon  { font-size: 18px; }
.file-name  { flex: 1; }
.file-pages {
  background: #ff6b3520; color: var(--accent);
  padding: 2px 10px; border-radius: 100px;
  font-size: 12px; font-weight: 600;
}
.remove-btn {
  background: none; border: none; color: var(--muted);
  font-size: 20px; cursor: pointer; transition: color 0.15s;
}
.remove-btn:hover { color: #ff6b6b; }

.pages-section  { margin-bottom: 20px; }
.pages-header   { display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; }
.pages-label    { font-size: 14px; font-weight: 500; color: var(--text2); }
.pages-label strong { color: #ff6b6b; }
.pages-actions  { display: flex; gap: 8px; }
.action-btn {
  padding: 5px 12px; border-radius: 7px; font-size: 12px;
  font-weight: 500; cursor: pointer; transition: all 0.15s;
  background: var(--surface2); border: 1px solid var(--border);
  color: var(--text2); font-family: 'DM Sans', sans-serif;
}
.action-btn:hover { border-color: var(--accent); color: var(--accent); }

.pages-grid {
  display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;
}
.page-btn {
  width: 42px; height: 42px; border-radius: 8px;
  border: 1px solid var(--border); background: var(--surface2);
  color: var(--text2); font-size: 13px; font-weight: 600;
  cursor: pointer; transition: all 0.15s;
  font-family: 'DM Sans', sans-serif;
}
.page-btn:hover   { border-color: var(--accent); color: var(--accent); }
.page-btn.selected {
  background: #ff6b6b20; border-color: #ff6b6b;
  color: #ff6b6b;
}

.selected-info { font-size: 13px; color: var(--muted); }

.loading-text { color: var(--muted); font-size: 13px; margin-bottom: 16px; }
.error-msg    { color: #ff6b6b; font-size: 13px; margin-bottom: 12px; }

.process-btn {
  width: 100%; padding: 13px; background: #ff6b6b; color: white;
  border: none; border-radius: 11px; font-size: 15px; font-weight: 600;
  cursor: pointer; font-family: 'DM Sans', sans-serif;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  transition: all 0.2s;
}
.process-btn:hover:not(:disabled) { background: #ff5252; transform: translateY(-1px); }
.process-btn:disabled { opacity: 0.45; cursor: not-allowed; }

.result-box {
  margin-top: 18px; background: #3ddc8412;
  border: 1px solid #3ddc8430; border-radius: 12px;
  padding: 20px; text-align: center;
}
.result-icon { font-size: 30px; margin-bottom: 8px; }
.result-text { font-size: 15px; font-weight: 600; color: var(--green); }
.result-sub  { font-size: 13px; color: var(--muted); margin: 4px 0 14px; }
.download-btn {
  display: inline-block; padding: 10px 24px;
  background: var(--green); color: #0a0a0f;
  border-radius: 9px; font-weight: 700; font-size: 14px;
  text-decoration: none; transition: opacity 0.2s;
}
.download-btn:hover { opacity: 0.85; }

@media (max-width: 768px) {
  .tool-card { padding: 20px 16px; }
  .pages-grid { gap: 6px; }
  .page-btn { width: 38px; height: 38px; font-size: 12px; }
}
</style>