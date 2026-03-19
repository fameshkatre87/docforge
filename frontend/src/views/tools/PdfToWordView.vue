<template>
  <AppLayout>
    <ToolCard
      title="PDF → Word"
      subtitle="Convert PDF to an editable Word document"
      icon="📄"
      drop-label="Click or drag a PDF here"
      hint="Extracts all text into a .docx file"
      accept=".pdf"
      :multiple="false"
      btn-label="📝 Convert to Word"
      :loading="loading"
      :progress="progress"
      :error="error"
      :result-url="resultUrl"
      result-filename="converted.docx"
      result-label="PDF converted to Word!"
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
  await process('/pdf/to-word/', files, { _filename: 'converted.docx' })
}
</script>
