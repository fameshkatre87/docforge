<template>
  <AppLayout>
    <ToolCard
      title="Compress PDF"
      subtitle="Reduce PDF file size without losing quality"
      icon="🗜️"
      drop-label="Click or drag a PDF here"
      hint="We'll compress streams to reduce file size"
      accept=".pdf"
      :multiple="false"
      btn-label="🗜️ Compress PDF"
      :loading="loading"
      :progress="progress"
      :error="error"
      :result-url="resultUrl"
      result-filename="compressed.pdf"
      result-label="PDF compressed successfully!"
      @process="run"
    />
  </AppLayout>
</template>

<script setup>
import AppLayout from '../../components/AppLayout.vue'
import ToolCard  from '../../components/ToolCard.vue'
import { useTool } from '../../composables/useTool'

const { loading, progress, error, resultUrl, process } = useTool()

async function run(files) {
  await process('/pdf/compress/', files, { _filename: 'compressed.pdf' })
}
</script>
