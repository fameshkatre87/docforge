<template>
  <AppLayout>
    <div class="fade-up">
      <h1 class="page-title">Admin Panel</h1>
      <p class="page-sub">Platform overview and user management</p>

      <!-- Stats -->
      <div class="stats-row" v-if="stats">
        <div class="stat-card">
          <p class="stat-label">Total Users</p>
          <p class="stat-val" style="color:var(--accent)">{{ stats.total_users }}</p>
        </div>
        <div class="stat-card">
          <p class="stat-label">Pro Users</p>
          <p class="stat-val" style="color:var(--purple)">{{ stats.pro_users }}</p>
        </div>
        <div class="stat-card">
          <p class="stat-label">Free Users</p>
          <p class="stat-val" style="color:var(--blue)">{{ stats.free_users }}</p>
        </div>
        <div class="stat-card">
          <p class="stat-label">Files Processed</p>
          <p class="stat-val" style="color:var(--green)">{{ stats.total_files_processed }}</p>
        </div>
      </div>

      <div v-if="statsError" class="error-msg">{{ statsError }}</div>

      <!-- Users Table -->
      <h2 class="section-title">All Users</h2>

      <div v-if="loadingUsers" class="loading-text">Loading users…</div>
      <div v-else-if="usersError" class="error-msg">{{ usersError }}</div>
      <div v-else class="table-wrap">
        <table class="users-table">
          <thead>
            <tr>
              <th>Username</th>
              <th>Email</th>
              <th>Plan</th>
              <th>Files</th>
              <th>Joined</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="u in users" :key="u.id">
              <td>{{ u.username }}</td>
              <td>{{ u.email }}</td>
              <td>
                <span class="plan-badge" :class="u.plan">{{ u.plan }}</span>
              </td>
              <td>{{ u.files_processed }}</td>
              <td>{{ formatDate(u.created_at) }}</td>
            </tr>
            <tr v-if="!users.length">
              <td colspan="5" style="text-align:center;color:var(--muted);padding:32px">No users found.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import AppLayout from '../components/AppLayout.vue'
import api from '../api/axios'

const stats       = ref(null)
const statsError  = ref('')
const users       = ref([])
const loadingUsers = ref(true)
const usersError  = ref('')

onMounted(async () => {
  // Fetch stats
  try {
    const { data } = await api.get('/auth/admin/stats/')
    stats.value = data
  } catch {
    statsError.value = 'Could not load stats.'
  }
  // Fetch users
  try {
    const { data } = await api.get('/auth/admin/users/')
    users.value = data
  } catch {
    usersError.value = 'Could not load users. Make sure you are a staff user.'
  } finally {
    loadingUsers.value = false
  }
})

function formatDate(dt) {
  if (!dt) return '—'
  return new Date(dt).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}
</script>

<style scoped>
.page-title { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 28px; }
.page-sub   { color: var(--muted); font-size: 15px; margin: 6px 0 32px; }

.stats-row {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 14px; margin-bottom: 38px;
}
.stat-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 14px; padding: 22px;
}
.stat-label { font-size: 11px; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.stat-val   { font-family: 'Syne', sans-serif; font-size: 30px; font-weight: 800; margin-top: 8px; }

.section-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 17px; margin-bottom: 16px; }

.table-wrap { overflow-x: auto; border-radius: 14px; border: 1px solid var(--border); }
.users-table { width: 100%; border-collapse: collapse; background: var(--surface); }
.users-table th {
  background: var(--surface2); padding: 13px 18px; text-align: left;
  font-size: 11px; font-weight: 600; color: var(--muted);
  text-transform: uppercase; letter-spacing: 0.5px;
}
.users-table td { padding: 13px 18px; font-size: 13.5px; border-top: 1px solid var(--border); }
.users-table tr:hover td { background: var(--surface2); }

.plan-badge {
  padding: 3px 10px; border-radius: 100px;
  font-size: 11px; font-weight: 600; text-transform: capitalize;
}
.plan-badge.free       { background: var(--surface2); color: var(--muted); }
.plan-badge.pro        { background: #ff6b3520; color: var(--accent); }
.plan-badge.enterprise { background: #b87cff20; color: var(--purple); }

.loading-text { color: var(--muted); font-size: 14px; padding: 20px 0; }
.error-msg    { color: #ff6b6b; font-size: 13px; margin-bottom: 16px; }
</style>
