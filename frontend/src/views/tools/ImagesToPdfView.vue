<template>
  <AppLayout>
    <ToolCard
      title="Images → PDF"
      subtitle="Convert multiple images into a single PDF file"
      icon="🖼️"
      drop-label="Click or drag images here"
      hint="Supports PNG, JPG, WEBP — order matters!"
      accept="image/*"
      :multiple="true"
      btn-label="📄 Convert to PDF"
      :loading="loading"
      :progress="progress"
      :error="error"
      :result-url="resultUrl"
      result-filename="images.pdf"
      result-label="Images converted to PDF!"
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
  await process('/pdf/images-to-pdf/', files, { _filename: 'images.pdf' })
}
</script>