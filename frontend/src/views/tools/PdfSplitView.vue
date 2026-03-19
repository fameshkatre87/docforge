<template>
  <AppLayout>
    <ToolCard
      title="Split PDF"
      subtitle="Divide a PDF into separate parts"
      icon="✂️"
      drop-label="Click or drag a PDF here"
      hint="Choose how many pages per chunk"
      accept=".pdf"
      :multiple="false"
      btn-label="✂️ Split PDF"
      :loading="loading"
      :progress="progress"
      :error="error"
      :result-url="resultUrl"
      result-filename="split_parts.zip"
      result-label="PDF split! Download the ZIP with all parts."
      @process="run"
    >
      <div class="opt-row">
        <label>Pages per chunk</label>
        <input v-model.number="pagesPerChunk" type="number" min="1" max="100" />
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
const pagesPerChunk = ref(1)

async function run(files) {
  await process('/pdf/split/', files, {
    pages_per_chunk: pagesPerChunk.value,
    _filename: 'split_parts.zip',
  })
}
</script>

<style scoped>
.opt-row {
  display: flex; align-items: center; gap: 14px;
  margin-bottom: 20px;
}
.opt-row label { font-size: 13px; font-weight: 500; color: var(--muted); white-space: nowrap; }
.opt-row input {
  width: 100px; background: var(--surface2); border: 1px solid var(--border);
  border-radius: 8px; padding: 9px 12px; color: var(--text);
  font-size: 14px; font-family: 'DM Sans', sans-serif; outline: none;
}
.opt-row input:focus { border-color: var(--accent); }
</style>
