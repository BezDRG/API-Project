<template>
  <div class="page">
    <header class="header">
      <div class="brand">Vue + FastAPI</div>
      <div class="hint">JWT • SQLAlchemy • Simple UI</div>
    </header>

    <main class="container">
      <AuthComponent
        v-if="!isAuth"
        @authorized="onAuthorized"
      />

      <UserDashboard
        v-else
        @logout="logout"
      />
    </main>

    <footer class="footer">
      © Demo project
    </footer>
  </div>
</template>

<script>
import AuthComponent from "./components/AuthComponent.vue";
import UserDashboard from "./components/UserDashboard.vue";

export default {
  name: "MainApp", // multi-word имя для eslint

  components: {
    AuthComponent,
    UserDashboard,
  },

  data() {
    return {
      isAuth: Boolean(localStorage.getItem("token")),
    };
  },

  methods: {
    onAuthorized(token) {
      localStorage.setItem("token", token);
      this.isAuth = true;
    },

    logout() {
      localStorage.removeItem("token");
      this.isAuth = false;
    },
  },
};
</script>

<style>
:root {
  --bg: #0b1220;
  --text: rgba(255, 255, 255, 0.92);
  --muted: rgba(255, 255, 255, 0.65);
  --line: rgba(255, 255, 255, 0.14);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  background: radial-gradient(
      900px 400px at 20% 10%,
      rgba(99, 102, 241, 0.25),
      transparent 60%
    ),
    radial-gradient(
      900px 400px at 80% 20%,
      rgba(16, 185, 129, 0.18),
      transparent 55%
    ),
    var(--bg);
  color: var(--text);
}

.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  padding: 24px 20px;
  border-bottom: 1px solid var(--line);
}

.brand {
  font-weight: 800;
  font-size: 18px;
}

.hint {
  margin-top: 6px;
  color: var(--muted);
  font-size: 13px;
}

.container {
  width: min(980px, 92vw);
  margin: 30px auto;
  flex: 1;
}

.footer {
  padding: 18px 20px;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 12px;
  text-align: center;
}
</style>