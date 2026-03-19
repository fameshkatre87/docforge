<template>
  <AppLayout>
    <div class="fade-up">
      <h1 class="page-title">Dashboard</h1>
      <p class="page-sub">Welcome back, {{ auth.userName }}!</p>

      <!-- Stats -->
      <div class="stats-row">
        <div class="stat-card">
          <p class="stat-label">Files Processed</p>
          <p class="stat-val" style="color:var(--accent)">{{ auth.user?.files_processed ?? 0 }}</p>
        </div>
        <div class="stat-card">
          <p class="stat-label">Current Plan</p>
          <p class="stat-val" style="color:var(--purple);text-transform:capitalize">{{ auth.userPlan }}</p>
        </div>
        <div class="stat-card">
          <p class="stat-label">Member Since</p>
          <p class="stat-val" style="color:var(--blue);font-size:18px">{{ joinedDate }}</p>
        </div>
      </div>

      <!-- Quick access tools -->
      <h2 class="section-title">Quick Tools</h2>
      <div class="tools-grid">
        <RouterLink v-for="tool in tools" :key="tool.path" :to="tool.path" class="tool-tile">
          <div class="tile-top">
            <span class="tile-icon">{{ tool.icon }}</span>
            <span class="tile-badge" :class="tool.type">{{ tool.type.toUpperCase() }}</span>
          </div>
          <p class="tile-name">{{ tool.name }}</p>
          <p class="tile-desc">{{ tool.desc }}</p>
        </RouterLink>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'
import AppLayout from '../components/AppLayout.vue'
import { useAuthStore } from '../stores/auth'

const auth = useAuthStore()

const joinedDate = computed(() => {
  if (!auth.user?.created_at) return '—'
  return new Date(auth.user.created_at).toLocaleDateString('en-US', { month: 'short', year: 'numeric' })
})
const tools = [
  { icon: '🔗', name: 'Merge PDFs',      desc: 'Combine multiple PDFs into one',      path: '/tools/pdf-merge',      type: 'pdf' },
  { icon: '✂️', name: 'Split PDF',       desc: 'Extract pages from any PDF',           path: '/tools/pdf-split',      type: 'pdf' },
  { icon: '📝', name: 'Word → PDF',      desc: 'Convert .docx to PDF instantly',       path: '/tools/word-to-pdf',    type: 'pdf' },
  { icon: '📄', name: 'PDF → Word',      desc: 'Convert PDF to editable .docx',        path: '/tools/pdf-to-word',    type: 'pdf' },
  { icon: '🗜️', name: 'Compress PDF',   desc: 'Reduce PDF file size',                 path: '/tools/pdf-compress',   type: 'pdf' },
  { icon: '🗑️', name: 'Remove Pages',   desc: 'Delete specific pages from PDF',       path: '/tools/remove-pages',   type: 'pdf' },
  { icon: '🖼️', name: 'Images → PDF',   desc: 'Convert images to PDF',                path: '/tools/images-to-pdf',  type: 'pdf' },
  { icon: '↔️', name: 'Resize Image',    desc: 'Resize to any dimension',              path: '/tools/image-resize',   type: 'image' },
  { icon: '🗜️', name: 'Compress Image', desc: 'Compress images with quality control', path: '/tools/image-compress', type: 'image' },
]

</script>



<style scoped>
.page-title { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 28px; }
.page-sub   { color: var(--muted); font-size: 15px; margin: 6px 0 32px; }

.stats-row {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
  gap: 14px; margin-bottom: 38px;
}
.stat-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 14px; padding: 22px;
}
.stat-label { font-size: 11px; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.stat-val   { font-family: 'Syne', sans-serif; font-size: 30px; font-weight: 800; margin-top: 8px; }

.section-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 17px; margin-bottom: 16px; }

.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 14px;
}
.tool-tile {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 13px; padding: 22px; text-decoration: none; color: var(--text);
  transition: all 0.2s; display: flex; flex-direction: column; gap: 8px;
}
.tool-tile:hover { border-color: var(--accent); transform: translateY(-2px); background: var(--surface2); }

.tile-top { display: flex; align-items: center; justify-content: space-between; }
.tile-icon { font-size: 22px; }
.tile-badge {
  font-size: 10px; font-weight: 700; padding: 2px 9px;
  border-radius: 100px; letter-spacing: 0.5px;
}
.tile-badge.pdf   { background: #ff6b3520; color: var(--accent); }
.tile-badge.image { background: #5b9cf620; color: var(--blue); }

.tile-name { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 14.5px; }
.tile-desc { color: var(--muted); font-size: 12.5px; }
@media (max-width: 768px) {
  .dash-title { font-size: 22px; }
  .header-badge { display: none; }
  .stats-row { grid-template-columns: repeat(2, 1fr) !important; gap: 10px; }
  .tools-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 10px; }
  .stat-value { font-size: 20px; }
  .tool-desc  { display: none; }
  .dash { padding: 0; }
}
</style>
