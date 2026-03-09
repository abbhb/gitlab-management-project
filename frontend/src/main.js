import Vue from 'vue'
import bkMagicVue from '@canway/cw-magic-vue'
import '@canway/cw-magic-vue/dist/bk-magic-vue.min.css'

import App from './App.vue'
import router from './router'
import appConfig from './config'
import './styles/global.css'

Vue.use(bkMagicVue)
Vue.config.productionTip = false
Vue.prototype.$appConfig = appConfig

new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app')
