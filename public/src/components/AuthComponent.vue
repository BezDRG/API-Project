<template>
  <div class="grid">
    <section class="card">
      <h2>Регистрация</h2>
      <p class="muted">Создайте аккаунт (пароль будет захеширован на сервере).</p>

      <form @submit.prevent="register">
        <label>Имя пользователя</label>
        <input v-model.trim="registerUsername" type="text" placeholder="например, marly" />

        <label>Возраст (необязательно)</label>
        <input v-model.number="registerAge" type="number" min="0" max="150" placeholder="25" />

        <label>Пароль</label>
        <input v-model="registerPassword" type="password" placeholder="минимум 6 символов" />

        <button :disabled="loading">Зарегистрироваться</button>
        <p v-if="errorRegister" class="error">{{ errorRegister }}</p>
        <p v-if="successRegister" class="success">{{ successRegister }}</p>
      </form>
    </section>

    <section class="card">
      <h2>Вход</h2>
      <p class="muted">Войдите и получите JWT токен.</p>

      <form @submit.prevent="login">
        <label>Имя пользователя</label>
        <input v-model.trim="loginUsername" type="text" placeholder="marly" />

        <label>Пароль</label>
        <input v-model="loginPassword" type="password" placeholder="ваш пароль" />

        <button :disabled="loading">Войти</button>
        <p v-if="errorLogin" class="error">{{ errorLogin }}</p>
      </form>
    </section>
  </div>
</template>

<script>
import api from "../api";

export default {
  name: "AuthComponent",
  data() {
    return {
      loading: false,

      registerUsername: "",
      registerAge: null,
      registerPassword: "",
      errorRegister: "",
      successRegister: "",

      loginUsername: "",
      loginPassword: "",
      errorLogin: "",
    };
  },
  methods: {
    async register() {
      this.errorRegister = "";
      this.successRegister = "";
      this.loading = true;

      try {
        await api.post("/auth/register", {
          username: this.registerUsername,
          age: this.registerAge ?? null,
          password: this.registerPassword,
        });

        this.successRegister = "Аккаунт создан. Теперь войдите справа.";
        this.registerPassword = "";
      } catch (e) {
        this.errorRegister = e?.response?.data?.detail || "Ошибка регистрации";
      } finally {
        this.loading = false;
      }
    },

    async login() {
      this.errorLogin = "";
      this.loading = true;

      try {
        const res = await api.post("/auth/login", {
          username: this.loginUsername,
          password: this.loginPassword,
        });

        this.$emit("authorized", res.data.access_token);
      } catch (e) {
        this.errorLogin = e?.response?.data?.detail || "Ошибка входа";
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.grid {
  display: grid;
  gap: 18px;
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

@media (max-width: 860px) {
  .grid { grid-template-columns: 1fr; }
}

.card {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.14);
  border-radius: 18px;
  padding: 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,.25);
}

h2 { margin: 0 0 6px; font-size: 18px; }
.muted { margin: 0 0 14px; color: rgba(255,255,255,.65); font-size: 13px; }

form { display: grid; gap: 10px; }
label { font-size: 12px; color: rgba(255,255,255,.7); }

input {
  width: 100%;
  padding: 10px 12px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,.16);
  background: rgba(0,0,0,.22);
  color: rgba(255,255,255,.92);
  outline: none;
}

input:focus { border-color: rgba(99,102,241,.6); }

button {
  margin-top: 4px;
  padding: 10px 12px;
  border-radius: 12px;
  border: 0;
  background: rgba(99,102,241,.9);
  color: white;
  font-weight: 700;
  cursor: pointer;
}

button:disabled { opacity: .55; cursor: not-allowed; }

.error { color: #ffb4b4; font-size: 13px; margin: 2px 0 0; }
.success { color: #b6ffd5; font-size: 13px; margin: 2px 0 0; }
</style>