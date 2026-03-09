<template>
  <div>
    <div class="page-head">
      <div>
        <h2 class="page-title">欢迎回来</h2>
        <p class="page-subtitle">集中查看项目、订阅与流水线通知的关键数据。</p>
      </div>
      <div class="inline-meta">
        <span class="path-chip">企业用户名：{{ summary.enterprise_username || '未绑定' }}</span>
      </div>
    </div>

    <div class="metrics-grid" v-bkloading="{ isLoading: loading }">
      <section class="metric-card">
        <p class="metric-card__label">可用项目</p>
        <h3 class="metric-card__value">{{ summary.project_count }}</h3>
        <bk-button theme="primary" @click="$router.push('/subscription/projects/')">查看项目</bk-button>
      </section>
      <section class="metric-card">
        <p class="metric-card__label">我的订阅</p>
        <h3 class="metric-card__value">{{ summary.subscription_count }}</h3>
        <bk-button theme="primary" @click="$router.push('/subscription/my-subscriptions/')">管理订阅</bk-button>
      </section>
      <section class="metric-card">
        <p class="metric-card__label">管理能力</p>
        <h3 class="metric-card__value">{{ summary.can_manage ? '是' : '否' }}</h3>
        <bk-button v-if="summary.can_manage" theme="primary" @click="$router.push('/subscription/projects/create/')">新增项目</bk-button>
        <bk-button v-else @click="$router.push('/subscription/projects/')">浏览项目</bk-button>
      </section>
    </div>

    <div class="two-column-grid">
      <section class="summary-card">
        <h3>最新项目</h3>
        <bk-table :data="summary.recent_projects" size="small" v-bkloading="{ isLoading: loading }">
          <bk-table-column label="项目" min-width="180">
            <template slot-scope="{ row }">
              <strong>{{ row.name }}</strong>
              <div class="inline-meta">{{ row.description || '暂无描述' }}</div>
            </template>
          </bk-table-column>
          <bk-table-column prop="default_branch" label="默认分支" width="120" />
          <bk-table-column prop="created_by_username" label="创建人" width="120" />
          <bk-table-column label="操作" width="120">
            <template slot-scope="{ row }">
              <bk-button text theme="primary" @click="$router.push(`/subscription/projects/${row.id}/`)">查看</bk-button>
            </template>
          </bk-table-column>
        </bk-table>
        <div v-if="!loading && !summary.recent_projects.length" class="empty-state">暂无项目数据。</div>
      </section>

      <section class="summary-card">
        <h3>工作流说明</h3>
        <bk-alert type="info" :show-icon="false" title="推荐流程：先建项目，再按目录/文件创建订阅，最后在 CI 中调用 Runner API。" />
        <div class="data-hint">
          <p>1. 管理员录入 GitLab 项目与访问令牌。</p>
          <p>2. 用户为目录或文件创建订阅规则。</p>
          <p>3. 流水线把变更文件传给 Runner API。</p>
          <p>4. 系统输出需要通知的企业用户名单。</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import { get } from '../services/api'

export default {
  name: 'DashboardPage',
  data() {
    return {
      loading: false,
      summary: {
        enterprise_username: '',
        project_count: 0,
        subscription_count: 0,
        can_manage: false,
        recent_projects: []
      }
    }
  },
  created() {
    this.loadSummary()
  },
  methods: {
    async loadSummary() {
      this.loading = true
      try {
        this.summary = await get('/api/dashboard/summary/')
      } catch (error) {
        this.$bkMessage({ theme: 'error', message: error.message || '首页数据加载失败' })
      } finally {
        this.loading = false
      }
    }
  }
}
</script>
