<template>
  <div class="landing">
    <div class="glow-one"></div>
    <div class="glow-two"></div>

    <!-- Nav -->
    <nav>
      <div class="logo"><span class="logo-box">📄</span> DocForge</div>
      <div class="nav-actions">
        <RouterLink to="/login"    class="btn-ghost">Log in</RouterLink>
        <RouterLink to="/register" class="btn-primary">Get Started →</RouterLink>
      </div>
    </nav>

    <!-- Hero -->
    <section class="hero">
      <div class="badge">✦ PDF & Image Management Platform</div>
      <h1>Process Files with<br><span>Professional Tools</span></h1>
      <p>Merge PDFs, convert Word docs, resize images, and manage your files — all in one powerful platform.</p>
      <div class="hero-btns">
        <RouterLink to="/dashboard" class="btn-primary btn-lg">Start Free →</RouterLink>
        <RouterLink to="/login"    class="btn-ghost btn-lg">Sign In</RouterLink>
      </div>
    </section>

    <!-- Tools Grid -->
    <section class="tools-grid">
      <!-- <div v-for="tool in tools" :key="tool.name" class="tool-card">
        <span class="t-icon">{{ tool.icon }}</span>
        <h3>{{ tool.name }}</h3>
        <p>{{ tool.desc }}</p>
      </div> -->
      <RouterLink v-for="tool in tools" :key="tool.name" :to="tool.path" class="tool-card">
        <span class="t-icon">{{ tool.icon }}</span>
        <h3>{{ tool.name }}</h3>
        <p>{{ tool.desc }}</p>
     </RouterLink>
    </section>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

// const tools = [
//   { icon: '🔗', name: 'Merge PDFs',    desc: 'Combine multiple PDFs into one document' },
//   { icon: '✂️', name: 'Split PDF',     desc: 'Extract or divide pages from any PDF' },
//   { icon: '📝', name: 'Word → PDF',    desc: 'Convert .docx files to PDF instantly' },
//   { icon: '📄', name: 'PDF → Word',    desc: 'Convert PDF to editable Word documents' },
//   { icon: '🗜️', name: 'Compress PDF', desc: 'Reduce PDF file size up to 70%' },
//   { icon: '🖼️', name: 'Image Tools',  desc: 'Resize and compress images easily' },
// ]

const tools = [
  { icon: '🔗', name: 'Merge PDFs',    desc: 'Combine multiple PDFs into one document', path: '/tools/pdf-merge' },
  { icon: '✂️', name: 'Split PDF',     desc: 'Extract or divide pages from any PDF',     path: '/tools/pdf-split' },
  { icon: '📝', name: 'Word → PDF',    desc: 'Convert .docx files to PDF instantly',      path: '/tools/word-to-pdf' },
  { icon: '📄', name: 'PDF → Word',    desc: 'Convert PDF to editable Word documents',    path: '/tools/pdf-to-word' },
  { icon: '🗑️', name: 'Remove Pages', desc: 'Delete specific pages from any PDF',        path: '/tools/remove-pages' },
  { icon: '🖼️', name: 'Image Tools',  desc: 'Resize and compress images easily',         path: '/tools/image-resize' },
]
</script>



<style scoped>
.landing { min-height: 100vh; position: relative; overflow: hidden; }

.glow-one {
  position: fixed; width: 500px; height: 500px;
  background: #ff6b3518; border-radius: 50%; filter: blur(120px);
  top: -120px; right: -100px; pointer-events: none; z-index: 0;
}
.glow-two {
  position: fixed; width: 400px; height: 400px;
  background: #5b9cf612; border-radius: 50%; filter: blur(100px);
  bottom: 0; left: -80px; pointer-events: none; z-index: 0;
}

nav {
  display: flex; align-items: center; justify-content: space-between;
  padding: 22px 48px; border-bottom: 1px solid var(--border);
  position: relative; z-index: 10;
}
.logo {
  font-family: 'Syne', sans-serif; font-weight: 800; font-size: 20px;
  display: flex; align-items: center; gap: 8px;
}
.logo-box {
  width: 30px; height: 30px; background: var(--accent); border-radius: 7px;
  display: flex; align-items: center; justify-content: center; font-size: 14px;
}
.nav-actions { display: flex; gap: 12px; align-items: center; }

.btn-ghost {
  padding: 9px 18px; border-radius: 9px; font-size: 14px; font-weight: 500;
  background: transparent; color: var(--text);
  border: 1px solid var(--border); text-decoration: none;
  transition: all 0.2s; cursor: pointer;
}
.btn-ghost:hover { border-color: var(--accent); color: var(--accent); }

.btn-primary {
  padding: 9px 18px; border-radius: 9px; font-size: 14px; font-weight: 600;
  background: var(--accent); color: white; border: none;
  text-decoration: none; transition: all 0.2s; cursor: pointer;
  box-shadow: 0 0 20px #ff6b3530;
}
.btn-primary:hover { background: var(--accent2); transform: translateY(-1px); }
.btn-lg { padding: 13px 26px; font-size: 16px; border-radius: 11px; }

.hero {
  display: flex; flex-direction: column; align-items: center;
  text-align: center; padding: 90px 40px 70px;
  position: relative; z-index: 5;
}
.badge {
  display: inline-flex; align-items: center;
  background: #ff6b3514; border: 1px solid #ff6b3530;
  color: var(--accent2); padding: 6px 16px; border-radius: 100px;
  font-size: 13px; font-weight: 500; margin-bottom: 28px;
  animation: fadeUp 0.5s ease both;
}
.hero h1 {
  font-family: 'Syne', sans-serif; font-weight: 800;
  font-size: clamp(40px, 5.5vw, 72px); line-height: 1.08;
  letter-spacing: -1.5px; max-width: 780px;
  animation: fadeUp 0.5s 0.08s ease both;
}
.hero h1 span { color: var(--accent); }
.hero p {
  margin-top: 22px; color: var(--muted); font-size: 17px;
  max-width: 500px; line-height: 1.7;
  animation: fadeUp 0.5s 0.16s ease both;
}
.hero-btns {
  display: flex; gap: 14px; margin-top: 36px;
  animation: fadeUp 0.5s 0.24s ease both;
}

.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px; padding: 0 48px 80px;
  max-width: 1100px; margin: 0 auto;
  position: relative; z-index: 5;
  animation: fadeUp 0.5s 0.32s ease both;
}
.tool-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 14px; padding: 26px 22px; cursor: pointer;
  transition: all 0.22s;
}
.tool-card:hover { border-color: var(--accent); transform: translateY(-3px); background: var(--surface2); }
.t-icon { font-size: 26px; display: block; margin-bottom: 14px; }
.tool-card h3 { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 14.5px; margin-bottom: 6px; }
.tool-card p  { color: var(--muted); font-size: 13px; line-height: 1.5; }

@media (max-width: 640px) {
  nav { padding: 16px 20px; }
  .hero { padding: 60px 20px 40px; }
  .tools-grid { padding: 0 16px 60px; }
}
@media (max-width: 640px) {
  nav { padding: 14px 16px; }
  .nav-actions .btn-ghost { display: none; }
  .hero { padding: 48px 16px 32px; }
  .hero h1 { font-size: 34px; letter-spacing: -0.5px; }
  .hero p  { font-size: 15px; }
  .hero-btns { flex-direction: column; width: 100%; }
  .hero-btns a { text-align: center; }
  .tools-grid { grid-template-columns: repeat(2, 1fr); padding: 0 16px 40px; gap: 10px; }
}
</style>
