<template>
  <div class="app-shell">
    <header class="app-header">
      <div class="app-header__inner">
        <div class="app-brand">
          <div class="app-brand__logo">GL</div>
          <div>
            <h1 class="app-brand__title">GitLab 订阅管理</h1>
            <p class="app-brand__desc">基于 cw-magic-vue 的统一前端工作台</p>
          </div>
        </div>
        <div class="app-header__nav">
          <bk-button
            v-for="item in navItems"
            :key="item.path"
            size="small"
            :theme="isActive(item) ? 'primary' : 'default'"
            @click="go(item.path)">
            {{ item.label }}
          </bk-button>
          <bk-tag theme="info">{{ userLabel }}</bk-tag>
          <bk-button v-if="config.urls.console" size="small" @click="open(config.urls.console)">蓝鲸控制台</bk-button>
          <bk-button v-if="config.urls.logout" size="small" @click="open(config.urls.logout)">退出登录</bk-button>
        </div>
      </div>
    </header>

    <main class="app-main">
      <router-view />
    </main>
  </div>
</template>

<script>
import appConfig from './config'

export default {
  name: 'App',
  data() {
    return {
      config: appConfig,
      navItems: [
        { label: '首页', path: '/' },
        { label: '项目列表', path: '/subscription/projects/' },
        { label: '我的订阅', path: '/subscription/my-subscriptions/' }
      ]
    }
  },
  computed: {
    userLabel() {
      if (this.config.user.enterprise_username) {
        return `${this.config.user.username} / ${this.config.user.enterprise_username}`
      }
      return this.config.user.username || '未登录'
    }
  },
  methods: {
    isActive(item) {
      if (item.path === '/') {
        return this.$route.path === '/'
      }
      return this.$route.path.startsWith(item.path)
    },
    go(path) {
      if (this.$route.path !== path) {
        this.$router.push(path)
      }
    },
    open(url) {
      window.location.href = url
    }
  }
}
</script>
