<template>
  <AppLayout>
    <ToolCard
      title="Word → PDF"
      subtitle="Convert Word documents to PDF format"
      icon="📝"
      drop-label="Click or drag your .docx file here"
      hint="Supports .doc and .docx formats"
      accept=".doc,.docx"
      :multiple="false"
      btn-label="📄 Convert to PDF"
      :loading="loading"
      :progress="progress"
      :error="error"
      :result-url="resultUrl"
      result-filename="converted.pdf"
      result-label="Word file converted to PDF!"
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
  await process('/pdf/from-word/', files, { _filename: 'converted.pdf' })
}
</script>
