<template>
  <AppLayout>
    <ToolCard
      title="Compress Image"
      subtitle="Reduce image file size with quality control"
      icon="🗜️"
      drop-label="Click or drag an image here"
      hint="Output will be JPEG for best compression"
      accept="image/*"
      :multiple="false"
      btn-label="🗜️ Compress Image"
      :loading="loading"
      :progress="progress"
      :error="error"
      :result-url="resultUrl"
      result-filename="compressed.jpg"
      result-label="Image compressed successfully!"
      @process="run"
    >
      <div class="quality-row">
        <label>Quality: <strong>{{ quality }}%</strong></label>
        <input v-model.number="quality" type="range" min="10" max="95" step="5" />
        <div class="quality-hints">
          <span>Smaller file</span>
          <span>Better quality</span>
        </div>
      </div>
    </ToolCard>
  </AppLayout>
</template>

<script setup>
import { ref } from 'vue'
import AppLayout from '../../components/AppLayout.vue'
import ToolCard  from '../../components/ToolCard.vue'
import { useTool } from '../../composables/useTool'

const { loading, progress, error, resultUrl, process } = useTool()
const quality = ref(70)

async function run(files) {
  await process('/image/compress/', files, {
    quality:   quality.value,
    _filename: 'compressed.jpg',
  })
}
</script>

<style scoped>
.quality-row {
  margin-bottom: 20px;
  display: flex; flex-direction: column; gap: 8px;
}
.quality-row label { font-size: 13px; font-weight: 500; color: var(--muted); }
.quality-row label strong { color: var(--text); }
.quality-row input[type="range"] {
  width: 100%; accent-color: var(--accent); cursor: pointer; height: 4px;
}
.quality-hints {
  display: flex; justify-content: space-between;
  font-size: 11px; color: var(--muted);
}
</style>
