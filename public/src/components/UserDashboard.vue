<template>
  <div class="wrap">
    <div class="topbar">
      <div>
        <div class="title">Вы авторизованы</div>
        <div class="muted" v-if="me">Пользователь: <b>{{ me.username }}</b></div>
      </div>
      <button class="ghost" @click="$emit('logout')">Выйти</button>
    </div>

    <div class="grid">
      <section class="card">
        <h3>Новый пост</h3>
        <form @submit.prevent="createPost">
          <input v-model.trim="title" placeholder="Заголовок" />
          <textarea v-model.trim="body" placeholder="Текст поста"></textarea>
          <button :disabled="loading">Опубликовать</button>
          <p v-if="error" class="error">{{ error }}</p>
        </form>
      </section>

      <section class="card">
        <h3>Лента</h3>
        <div v-if="loading && posts.length === 0" class="muted">Загрузка...</div>

        <div v-for="p in posts" :key="p.id" class="post">
          <div class="postTitle">{{ p.title }}</div>
          <div class="postBody">{{ p.body }}</div>
          <div class="postMeta">
            <span>Автор: {{ p.author.username }}</span>
            <span>•</span>
            <span>{{ formatDate(p.created_at) }}</span>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import api from "../api";

export default {
  name: "UserDashboard",
  data() {
    return {
      me: null,
      posts: [],
      title: "",
      body: "",
      loading: false,
      error: "",
    };
  },
  async mounted() {
    await this.bootstrap();
  },
  methods: {
    async bootstrap() {
      this.loading = true;
      this.error = "";
      try {
        const [meRes, postsRes] = await Promise.all([
          api.get("/users/me"),
          api.get("/posts"),
        ]);
        this.me = meRes.data;
        this.posts = postsRes.data;
      } catch (e) {
        this.error = e?.response?.data?.detail || "Не удалось загрузить данные";
      } finally {
        this.loading = false;
      }
    },

    async createPost() {
      this.error = "";
      this.loading = true;

      try {
        const res = await api.post("/posts", { title: this.title, body: this.body });
        this.posts = [res.data, ...this.posts];
        this.title = "";
        this.body = "";
      } catch (e) {
        this.error = e?.response?.data?.detail || "Не удалось создать пост";
      } finally {
        this.loading = false;
      }
    },

    formatDate(iso) {
      const d = new Date(iso);
      return d.toLocaleString();
    },
  },
};
</script>

<style scoped>
.wrap { display: grid; gap: 16px; }
.topbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px; border: 1px solid rgba(255,255,255,.14);
  background: rgba(255,255,255,.06); border-radius: 18px;
}

.title { font-size: 16px; font-weight: 800; }
.muted { color: rgba(255,255,255,.65); font-size: 13px; margin-top: 4px; }

.grid { display: grid; gap: 18px; grid-template-columns: 360px 1fr; }
@media (max-width: 900px) { .grid { grid-template-columns: 1fr; } }

.card {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.14);
  border-radius: 18px;
  padding: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,.25);
}

h3 { margin: 0 0 10px; font-size: 16px; }

form { display: grid; gap: 10px; }
input, textarea {
  width: 100%;
  padding: 10px 12px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,.16);
  background: rgba(0,0,0,.22);
  color: rgba(255,255,255,.92);
  outline: none;
}
textarea { min-height: 120px; resize: vertical; }
input:focus, textarea:focus { border-color: rgba(16,185,129,.6); }

button {
  padding: 10px 12px;
  border-radius: 12px;
  border: 0;
  background: rgba(16,185,129,.9);
  color: white;
  font-weight: 800;
  cursor: pointer;
}
button:disabled { opacity: .55; cursor: not-allowed; }

.ghost {
  background: transparent;
  border: 1px solid rgba(255,255,255,.18);
  color: rgba(255,255,255,.9);
  padding: 10px 12px;
  border-radius: 12px;
  cursor: pointer;
}
.ghost:hover { background: rgba(255,255,255,.06); }

.post {
  padding: 12px;
  border: 1px solid rgba(255,255,255,.12);
  background: rgba(255,255,255,.05);
  border-radius: 14px;
  margin-top: 10px;
}
.postTitle { font-weight: 900; }
.postBody { margin-top: 6px; color: rgba(255,255,255,.86); white-space: pre-wrap; }
.postMeta { margin-top: 8px; color: rgba(255,255,255,.6); font-size: 12px; display: flex; gap: 8px; }
.error { color: #ffb4b4; font-size: 13px; margin-top: 8px; }
</style>