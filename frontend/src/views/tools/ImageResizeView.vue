<template>
  <AppLayout>
    <ToolCard
      title="Resize Image"
      subtitle="Resize any image to exact dimensions"
      icon="↔️"
      drop-label="Click or drag an image here"
      hint="Supports PNG, JPG, WEBP, GIF"
      accept="image/*"
      :multiple="false"
      btn-label="↔️ Resize Image"
      :loading="loading"
      :progress="progress"
      :error="error"
      :result-url="resultUrl"
      :result-filename="resultFilename"
      result-label="Image resized successfully!"
      @process="run"
    >
      <div class="options">
        <div class="opt-field">
          <label>Width (px)</label>
          <input v-model.number="width" type="number" min="1" max="8000" />
        </div>
        <div class="opt-field">
          <label>Height (px)</label>
          <input v-model.number="height" type="number" min="1" max="8000" />
        </div>
        <div class="opt-check">
          <input id="aspect" v-model="maintainAspect" type="checkbox" />
          <label for="aspect">Maintain aspect ratio</label>
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

const { loading, progress, error, resultUrl, resultFilename, process } = useTool()

const width         = ref(800)
const height        = ref(600)
const maintainAspect = ref(false)

async function run(files) {
  await process('/image/resize/', files, {
    width:           width.value,
    height:          height.value,
    maintain_aspect: maintainAspect.value ? 'true' : 'false',
    _filename:       `resized_${width.value}x${height.value}.jpg`,
  })
}
</script>

<style scoped>
.options { margin-bottom: 20px; display: flex; flex-wrap: wrap; gap: 14px; align-items: flex-end; }

.opt-field { display: flex; flex-direction: column; gap: 7px; }
.opt-field label { font-size: 13px; font-weight: 500; color: var(--muted); }
.opt-field input {
  width: 110px; background: var(--surface2); border: 1px solid var(--border);
  border-radius: 8px; padding: 9px 12px; color: var(--text);
  font-size: 14px; font-family: 'DM Sans', sans-serif; outline: none;
}
.opt-field input:focus { border-color: var(--accent); }

.opt-check {
  display: flex; align-items: center; gap: 8px;
  padding-bottom: 10px;
}
.opt-check label { font-size: 13px; color: var(--muted); cursor: pointer; }
.opt-check input[type="checkbox"] {
  width: 16px; height: 16px; accent-color: var(--accent); cursor: pointer;
}
</style>
