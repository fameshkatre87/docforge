<template>
  <div class="layout">

    <!-- Mobile Top Bar -->
    <div class="mobile-topbar">
      <div class="mobile-logo">
        <span class="logo-box">📄</span> DocForge
      </div>
      <button class="hamburger" @click="menuOpen = !menuOpen">
        <span v-if="!menuOpen">☰</span>
        <span v-else>✕</span>
      </button>
    </div>

    <!-- Overlay -->
    <div v-if="menuOpen" class="overlay" @click="menuOpen = false"></div>

    <!-- Sidebar -->
    <aside class="sidebar" :class="{ open: menuOpen }">
      <div class="sidebar-logo">
        <div class="logo-mark"><span>📄</span></div>
        <span class="logo-text">DocForge</span>
      </div>

      <nav class="sidebar-nav">
        <div class="nav-group">
          <p class="nav-label">Overview</p>
          <RouterLink to="/dashboard" class="nav-item" @click="menuOpen = false">
            <span class="nav-icon">⊞</span><span>Dashboard</span>
          </RouterLink>
        </div>

        <div class="nav-group">
          <p class="nav-label">PDF Tools</p>
          <RouterLink to="/tools/pdf-merge"    class="nav-item" @click="menuOpen = false"><span class="nav-icon">🔗</span><span>Merge PDFs</span></RouterLink>
          <RouterLink to="/tools/pdf-split"    class="nav-item" @click="menuOpen = false"><span class="nav-icon">✂️</span><span>Split PDF</span></RouterLink>
          <RouterLink to="/tools/word-to-pdf"  class="nav-item" @click="menuOpen = false"><span class="nav-icon">📝</span><span>Word → PDF</span></RouterLink>
          <RouterLink to="/tools/pdf-to-word"  class="nav-item" @click="menuOpen = false"><span class="nav-icon">📄</span><span>PDF → Word</span></RouterLink>
          <RouterLink to="/tools/pdf-compress" class="nav-item" @click="menuOpen = false"><span class="nav-icon">🗜️</span><span>Compress PDF</span></RouterLink>
          <RouterLink to="/tools/remove-pages" class="nav-item" @click="menuOpen = false"><span class="nav-icon">🗑️</span><span>Remove Pages</span></RouterLink>
          <RouterLink to="/tools/images-to-pdf" class="nav-item" @click="menuOpen = false"><span class="nav-icon">🖼️</span><span>Images → PDF</span></RouterLink>
        </div>

        <div class="nav-group">
          <p class="nav-label">Image Tools</p>
          <RouterLink to="/tools/image-resize"   class="nav-item" @click="menuOpen = false"><span class="nav-icon">↔️</span><span>Resize Image</span></RouterLink>
          <RouterLink to="/tools/image-compress" class="nav-item" @click="menuOpen = false"><span class="nav-icon">🗜️</span><span>Compress Image</span></RouterLink>
        </div>

        <div v-if="auth.isAdmin" class="nav-group">
          <p class="nav-label">System</p>
          <RouterLink to="/admin" class="nav-item" @click="menuOpen = false"><span class="nav-icon">🛡️</span><span>Admin Panel</span></RouterLink>
        </div>
      </nav>

      <div class="sidebar-footer">
        <div v-if="auth.isLoggedIn" class="user-card">
          <div class="user-avatar">{{ auth.userName[0].toUpperCase() }}</div>
          <div class="user-details">
            <p class="user-name">{{ auth.userName }}</p>
            <span class="user-plan">{{ auth.userPlan }}</span>
          </div>
          <button class="logout-icon" @click="logout" title="Logout">⏻</button>
        </div>
        <div v-else class="auth-buttons">
          <RouterLink to="/login"    class="btn-signin"     @click="menuOpen = false">Sign In</RouterLink>
          <RouterLink to="/register" class="btn-getstarted" @click="menuOpen = false">Get Started →</RouterLink>
        </div>
      </div>
    </aside>

    <main class="main-area">
      <slot />
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const auth     = useAuthStore()
const router   = useRouter()
const menuOpen = ref(false)

function logout() {
  auth.logout()
  menuOpen.value = false
  router.push('/')
}
</script>

<style scoped>
.layout { display: flex; min-height: 100vh; }

/* ── Mobile Top Bar ── */
.mobile-topbar {
  display: none;
  position: fixed; top: 0; left: 0; right: 0; z-index: 200;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 16px;
  height: 56px;
  align-items: center;
  justify-content: space-between;
}
.mobile-logo {
  font-family: 'Syne', sans-serif;
  font-weight: 800; font-size: 17px;
  display: flex; align-items: center; gap: 8px;
}
.hamburger {
  background: none; border: 1px solid var(--border);
  color: var(--text); font-size: 18px;
  width: 36px; height: 36px; border-radius: 8px;
  cursor: pointer; display: flex;
  align-items: center; justify-content: center;
  transition: all 0.2s;
}
.hamburger:hover { border-color: var(--accent); color: var(--accent); }

/* ── Overlay ── */
.overlay {
  display: none;
  position: fixed; inset: 0; z-index: 150;
  background: #00000070;
  backdrop-filter: blur(2px);
}

/* ── Sidebar ── */
.sidebar {
  width: 248px; flex-shrink: 0;
  background: var(--surface);
  border-right: 1px solid var(--border);
  display: flex; flex-direction: column;
  position: sticky; top: 0; height: 100vh;
  overflow-y: auto; z-index: 160;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.sidebar-logo {
  display: flex; align-items: center; gap: 10px;
  padding: 20px 18px 18px;
  border-bottom: 1px solid var(--border);
}
.logo-mark {
  width: 34px; height: 34px;
  background: linear-gradient(135deg, var(--accent), #ff9a5c);
  border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
  font-size: 16px;
  box-shadow: 0 4px 12px var(--accent-glow);
}
.logo-text {
  font-family: 'Syne', sans-serif;
  font-weight: 800; font-size: 18px;
  background: linear-gradient(135deg, #fff, #c8c4d4);
  /* -webkit-background-clip: text; -webkit-text-fill-color: transparent; */
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.sidebar-nav { flex: 1; padding: 12px 10px; overflow-y: auto; }
.nav-group { margin-bottom: 6px; }
.nav-label {
  font-size: 10px; font-weight: 700;
  letter-spacing: 1.2px; text-transform: uppercase;
  color: var(--muted); padding: 10px 10px 5px;
}
.nav-item {
  display: flex; align-items: center; gap: 9px;
  padding: 9px 10px; border-radius: 8px;
  color: var(--text2); text-decoration: none;
  font-size: 13.5px; font-weight: 500;
  transition: all 0.15s; margin-bottom: 1px;
}
.nav-item:hover { background: var(--surface2); color: var(--text); }
.nav-item.router-link-active {
  background: linear-gradient(135deg, #ff6b3518, #ff6b350a);
  color: var(--accent);
  border: 1px solid #ff6b3520;
}
.nav-icon { font-size: 15px; width: 20px; text-align: center; flex-shrink: 0; }

.sidebar-footer {
  padding: 12px 10px;
  border-top: 1px solid var(--border);
}
.user-card {
  display: flex; align-items: center; gap: 9px;
  background: var(--surface2); border: 1px solid var(--border);
  border-radius: 10px; padding: 10px 12px;
}
.user-avatar {
  width: 32px; height: 32px; border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), var(--purple));
  display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 13px; color: white; flex-shrink: 0;
}
.user-details { flex: 1; min-width: 0; }
.user-name { font-size: 12.5px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.user-plan {
  font-size: 10px; color: var(--green);
  background: #3ddc8418; padding: 1px 7px;
  border-radius: 100px; font-weight: 600;
  text-transform: capitalize; display: inline-block; margin-top: 2px;
}
.logout-icon {
  background: none; border: none; color: var(--muted);
  font-size: 16px; cursor: pointer; padding: 4px;
  border-radius: 6px; transition: all 0.15s; flex-shrink: 0;
}
.logout-icon:hover { color: #ff6b6b; background: #ff6b6b15; }

.auth-buttons { display: flex; flex-direction: column; gap: 8px; }
.btn-signin {
  display: block; text-align: center; padding: 9px;
  color: var(--text2); text-decoration: none;
  font-size: 13px; font-weight: 500;
  border-radius: 8px; border: 1px solid var(--border2);
  transition: all 0.15s;
}
.btn-signin:hover { color: var(--text); border-color: var(--accent); }
.btn-getstarted {
  display: block; text-align: center; padding: 9px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  color: white; text-decoration: none;
  font-size: 13px; font-weight: 600; border-radius: 8px;
  box-shadow: 0 4px 14px var(--accent-glow);
  transition: all 0.15s;
}
.btn-getstarted:hover { transform: translateY(-1px); }

/* ── Main ── */
.main-area {
  flex: 1; padding: 36px 40px;
  background: var(--bg); overflow-y: auto;
}

/* ── MOBILE ── */
@media (max-width: 768px) {
  .mobile-topbar { display: flex; }
  .overlay       { display: block; }

  .sidebar {
    position: fixed;
    top: 0; left: 0;
    height: 100vh;
    transform: translateX(-100%);
    box-shadow: 4px 0 24px #00000060;
  }
  .sidebar.open { transform: translateX(0); }

  .main-area {
    padding: 76px 16px 24px;
    width: 100%;
  }
}
</style>