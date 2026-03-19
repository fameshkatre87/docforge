<template>
  <AppLayout>
    <ToolCard
      title="Merge PDFs"
      subtitle="Combine multiple PDF files into one document"
      icon="🔗"
      drop-label="Click or drag PDF files here"
      hint="Select 2 or more PDF files"
      accept=".pdf"
      :multiple="true"
      btn-label="🔗 Merge PDFs"
      :loading="loading"
      :progress="progress"
      :error="error"
      :result-url="resultUrl"
      result-filename="merged.pdf"
      result-label="PDFs merged successfully!"
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
  await process('/pdf/merge/', files, { _filename: 'merged.pdf' })
}
</script>
