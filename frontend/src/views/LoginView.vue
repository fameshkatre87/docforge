<template>
  <div class="auth-page">
    <div class="auth-card fade-up">
      <RouterLink to="/" class="back-link">← Back</RouterLink>
      <div class="logo"><span class="logo-box">📄</span> DocForge</div>
      <h2>Welcome back</h2>
      <p class="sub">Sign in to your account</p>

      <div class="field">
        <label>Email</label>
        <input v-model="email" type="email" placeholder="you@example.com" @keyup.enter="submit" />
      </div>
      <div class="field">
        <label>Password</label>
        <input v-model="password" type="password" placeholder="••••••••" @keyup.enter="submit" />
      </div>

      <button class="submit-btn" :disabled="loading" @click="submit">
        <span v-if="loading" class="spinner"></span>
        <span v-else>Sign In</span>
      </button>

      <p v-if="error" class="error">{{ error }}</p>

      <p class="switch">No account? <RouterLink to="/register">Sign up free</RouterLink></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const auth     = useAuthStore()
const router   = useRouter()
const email    = ref('')
const password = ref('')
const loading  = ref(false)
const error    = ref('')

async function submit() {
  error.value = ''
  if (!email.value || !password.value) { error.value = 'Please fill all fields.'; return }
  loading.value = true
  try {
    await auth.login(email.value, password.value)
    router.push('/dashboard')
  } catch (e) {
    error.value = e.response?.data?.error || 'Login failed. Check credentials.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-page {
  min-height: 100vh; display: flex;
  align-items: center; justify-content: center;
  background: var(--bg); padding: 20px;
}
.auth-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 22px; padding: 44px 40px;
  width: 100%; max-width: 420px; position: relative;
}
.back-link {
  display: inline-block; color: var(--muted); text-decoration: none;
  font-size: 13px; margin-bottom: 24px; transition: color 0.15s;
}
.back-link:hover { color: var(--text); }
.logo {
  font-family: 'Syne', sans-serif; font-weight: 800; font-size: 18px;
  display: flex; align-items: center; gap: 8px; margin-bottom: 24px;
}
.logo-box {
  width: 28px; height: 28px; background: var(--accent); border-radius: 7px;
  display: flex; align-items: center; justify-content: center; font-size: 13px;
}
h2   { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 26px; }
.sub { color: var(--muted); font-size: 14px; margin: 6px 0 28px; }

.field { margin-bottom: 18px; }
.field label {
  display: block; font-size: 13px; font-weight: 500;
  color: var(--muted); margin-bottom: 7px;
}
.field input {
  width: 100%; background: var(--surface2); border: 1px solid var(--border);
  border-radius: 9px; padding: 11px 14px; color: var(--text);
  font-size: 14px; font-family: 'DM Sans', sans-serif;
  outline: none; transition: border-color 0.2s;
}
.field input:focus { border-color: var(--accent); }

.submit-btn {
  width: 100%; margin-top: 6px; padding: 13px;
  background: var(--accent); color: white; border: none;
  border-radius: 10px; font-size: 15px; font-weight: 600;
  cursor: pointer; font-family: 'DM Sans', sans-serif;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  transition: all 0.2s;
}
.submit-btn:hover:not(:disabled) { background: var(--accent2); transform: translateY(-1px); }
.submit-btn:disabled { opacity: 0.5; cursor: not-allowed; }

.error  { color: #ff6b6b; font-size: 13px; margin-top: 12px; text-align: center; }
.switch { text-align: center; margin-top: 22px; color: var(--muted); font-size: 14px; }
.switch a { color: var(--accent); text-decoration: none; font-weight: 500; }
.switch a:hover { text-decoration: underline; }
</style>
