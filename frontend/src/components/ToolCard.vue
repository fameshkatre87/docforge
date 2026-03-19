<template>
  <div class="tool-card fade-up">
    <div class="card-header">
      <div>
        <h1 class="card-title">{{ title }}</h1>
        <p class="card-sub">{{ subtitle }}</p>
      </div>
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
      <span class="upload-icon">{{ icon }}</span>
      <p class="upload-title">{{ dropLabel }}</p>
      <p class="upload-hint">{{ hint }}</p>
      <input
        ref="fileInput"
        type="file"
        :multiple="multiple"
        :accept="accept"
        style="display:none"
        @change="onFileChange"
      />
    </div>

    <!-- File List -->
    <div v-if="files.length" class="file-list">
      <div v-for="(f, i) in files" :key="i" class="file-item">
        <span class="file-icon">{{ fileIcon(f) }}</span>
        <span class="file-name">{{ f.name }}</span>
        <span class="file-size">{{ formatSize(f.size) }}</span>
        <button class="remove-btn" @click.stop="removeFile(i)">×</button>
      </div>
    </div>

    <!-- Extra slot (e.g. options inputs) -->
    <slot />

    <!-- Progress bar -->
    <div v-if="progress > 0 && progress < 100" class="progress-wrap">
      <div class="progress-bar" :style="{ width: progress + '%' }"></div>
    </div>

    <!-- Action Button -->
    <button class="process-btn" :disabled="!files.length || loading" @click="$emit('process', files)">
      <span v-if="loading" class="spinner"></span>
      <span v-else>{{ btnLabel }}</span>
    </button>

    <!-- Error -->
    <p v-if="error" class="error-msg">⚠ {{ error }}</p>

    <!-- Success -->
    <div v-if="resultUrl" class="result-box">
      <p class="result-text">✅ {{ resultLabel }}</p>
      <a :href="resultUrl" :download="resultFilename" class="download-btn">
        ⬇ Download File
      </a>
    </div>
  </div>
</template>



<script setup>
import { ref } from 'vue'

const props = defineProps({
  title:          String,
  subtitle:       String,
  icon:           { type: String, default: '📂' },
  dropLabel:      { type: String, default: 'Click or drag files here' },
  hint:           String,
  accept:         { type: String, default: '*' },
  multiple:       { type: Boolean, default: false },
  btnLabel:       { type: String, default: 'Process' },
  loading:        { type: Boolean, default: false },
  progress:       { type: Number, default: 0 },
  error:          { type: String, default: '' },
  resultUrl:      { type: String, default: '' },
  resultFilename: { type: String, default: 'result' },
  resultLabel:    { type: String, default: 'Done! File is ready.' },
})

const emit = defineEmits(['process', 'update:files'])

const files     = ref([])
const isDragging = ref(false)

function onFileChange(e) {
  addFiles(Array.from(e.target.files))
  e.target.value = ''
}
function onDrop(e) {
  isDragging.value = false
  addFiles(Array.from(e.dataTransfer.files))
}
function addFiles(newFiles) {
  if (props.multiple) files.value.push(...newFiles)
  else                files.value = [newFiles[0]]
}
function removeFile(i) { files.value.splice(i, 1) }

function fileIcon(f) {
  if (f.type.includes('pdf'))   return '📄'
  if (f.type.includes('word') || f.name.endsWith('.docx') || f.name.endsWith('.doc')) return '📝'
  if (f.type.includes('image')) return '🖼️'
  return '📎'
}
function formatSize(bytes) {
  if (bytes < 1024)        return bytes + ' B'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB'
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB'
}
</script>

<style scoped>
.tool-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px; padding: 36px;
  max-width: 640px;
}
.card-header { margin-bottom: 28px; }
.card-title  { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 26px; }
.card-sub    { color: var(--muted); font-size: 14px; margin-top: 6px; }

.upload-zone {
  border: 2px dashed var(--border); border-radius: 13px;
  padding: 44px 24px; text-align: center; cursor: pointer;
  transition: all 0.2s; margin-bottom: 20px;
}
.upload-zone:hover, .upload-zone.dragging {
  border-color: var(--accent); background: #ff6b3508;
}
.upload-icon  { font-size: 44px; display: block; margin-bottom: 14px; }
.upload-title { font-size: 15px; font-weight: 500; }
.upload-hint  { color: var(--muted); font-size: 13px; margin-top: 6px; }

.file-list { display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px; }
.file-item {
  display: flex; align-items: center; gap: 10px;
  background: var(--surface2); border-radius: 9px; padding: 11px 14px;
  font-size: 13.5px;
}
.file-icon { font-size: 18px; }
.file-name { flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.file-size { color: var(--muted); font-size: 12px; white-space: nowrap; }
.remove-btn {
  background: none; border: none; color: var(--muted);
  font-size: 18px; cursor: pointer; line-height: 1; padding: 0 2px;
  transition: color 0.15s;
}
.remove-btn:hover { color: #ff6b6b; }

.progress-wrap {
  height: 4px; background: var(--surface2); border-radius: 2px; margin-bottom: 16px; overflow: hidden;
}
.progress-bar { height: 100%; background: var(--accent); border-radius: 2px; transition: width 0.3s; }

.process-btn {
  width: 100%; padding: 13px; background: var(--accent); color: white;
  border: none; border-radius: 11px; font-size: 15px; font-weight: 600;
  cursor: pointer; transition: all 0.2s; font-family: 'DM Sans', sans-serif;
  display: flex; align-items: center; justify-content: center; gap: 8px;
}
.process-btn:hover:not(:disabled) { background: var(--accent2); transform: translateY(-1px); }
.process-btn:disabled { opacity: 0.45; cursor: not-allowed; transform: none; }

.error-msg { color: #ff6b6b; font-size: 13px; margin-top: 12px; }

.result-box {
  margin-top: 18px; background: #3ddc8412;
  border: 1px solid #3ddc8430; border-radius: 12px;
  padding: 20px; text-align: center;
}
.result-text { font-size: 15px; font-weight: 600; color: var(--green); margin-bottom: 14px; }
.download-btn {
  display: inline-block; padding: 10px 24px;
  background: var(--green); color: #0a0a0f;
  border-radius: 9px; font-weight: 700; font-size: 14px;
  text-decoration: none; transition: opacity 0.2s;
}
.download-btn:hover { opacity: 0.85; }

@media (max-width: 768px) {
  .tool-card { padding: 24px 16px; }
  .upload-zone { padding: 32px 16px; }
  .upload-icon { font-size: 36px; }
}
</style>
