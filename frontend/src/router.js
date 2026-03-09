import Vue from 'vue'
import VueRouter from 'vue-router'

import DashboardPage from './pages/DashboardPage.vue'
import ProjectListPage from './pages/ProjectListPage.vue'
import ProjectFormPage from './pages/ProjectFormPage.vue'
import ProjectDetailPage from './pages/ProjectDetailPage.vue'
import SubscriptionListPage from './pages/SubscriptionListPage.vue'
import SubscriptionFormPage from './pages/SubscriptionFormPage.vue'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: DashboardPage,
      meta: { title: '首页' }
    },
    {
      path: '/subscription/projects/',
      name: 'project-list',
      component: ProjectListPage,
      meta: { title: '项目列表' }
    },
    {
      path: '/subscription/projects/create/',
      name: 'project-create',
      component: ProjectFormPage,
      props: { mode: 'create' },
      meta: { title: '新增项目' }
    },
    {
      path: '/subscription/projects/:projectId/edit/',
      name: 'project-edit',
      component: ProjectFormPage,
      props: (route) => ({ mode: 'edit', projectId: route.params.projectId }),
      meta: { title: '编辑项目' }
    },
    {
      path: '/subscription/projects/:projectId/',
      name: 'project-detail',
      component: ProjectDetailPage,
      props: true,
      meta: { title: '项目详情' }
    },
    {
      path: '/subscription/projects/:projectId/subscribe/',
      name: 'subscription-create',
      component: SubscriptionFormPage,
      props: true,
      meta: { title: '新增订阅' }
    },
    {
      path: '/subscription/my-subscriptions/',
      name: 'subscription-list',
      component: SubscriptionListPage,
      meta: { title: '我的订阅' }
    },
    {
      path: '*',
      redirect: '/'
    }
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  }
})

router.afterEach((to) => {
  document.title = `${to.meta.title || 'GitLab订阅管理'} - GitLab订阅管理`
})

export default router
