<template>
  <div v-bkloading="{ isLoading: loading }">
    <section class="page-card">
      <div class="page-head">
        <div>
          <h2 class="page-title">{{ project.name || '项目详情' }}</h2>
          <p class="page-subtitle">{{ project.description || '查看当前项目的订阅规则与分支信息。' }}</p>
          <div class="inline-meta">
            <span class="path-chip">默认分支：{{ project.default_branch || '--' }}</span>
            <span class="path-chip">GitLab 项目 ID：{{ project.gitlab_project_id || '--' }}</span>
          </div>
        </div>
        <div class="form-actions">
          <bk-button theme="primary" @click="goCreateSubscription">新增订阅</bk-button>
          <bk-button v-if="canManage" @click="goEditProject">编辑项目</bk-button>
          <bk-button @click="$router.push('/subscription/projects/')">返回</bk-button>
        </div>
      </div>

      <div class="toolbar">
        <bk-button @click="openGitlab">打开 GitLab</bk-button>
        <bk-button @click="loadProject">刷新</bk-button>
      </div>

      <bk-table :data="subscriptions" size="small" outer-border>
        <bk-table-column prop="path" label="订阅路径" min-width="260" />
        <bk-table-column label="类型" width="120">
          <template slot-scope="{ row }">{{ row.path_type === 'directory' ? '目录' : '文件' }}</template>
        </bk-table-column>
        <bk-table-column prop="branch" label="目标分支" width="140" />
        <bk-table-column label="创建时间" width="180">
          <template slot-scope="{ row }">{{ formatDate(row.created_at) }}</template>
        </bk-table-column>
        <bk-table-column label="操作" width="120" fixed="right">
          <template slot-scope="{ row }">
            <bk-button text theme="danger" @click="deleteSubscription(row)">删除</bk-button>
          </template>
        </bk-table-column>
      </bk-table>

      <div v-if="!loading && !subscriptions.length" class="empty-state">你还没有为该项目创建任何订阅。</div>
    </section>
  </div>
</template>

<script>
import { del, get } from '../services/api'

export default {
  name: 'ProjectDetailPage',
  props: {
    projectId: {
      type: [String, Number],
      required: true
    }
  },
  data() {
    return {
      loading: false,
      canManage: false,
      project: {},
      subscriptions: []
    }
  },
  created() {
    this.loadProject()
  },
  methods: {
    async loadProject() {
      this.loading = true
      try {
        const result = await get(`/api/projects/${this.projectId}/`)
        this.project = result.project || {}
        this.subscriptions = result.subscriptions || []
        this.canManage = Boolean(result.can_manage)
      } catch (error) {
        this.$bkMessage({ theme: 'error', message: error.message || '项目详情加载失败' })
      } finally {
        this.loading = false
      }
    },
    goCreateSubscription() {
      this.$router.push(`/subscription/projects/${this.projectId}/subscribe/`)
    },
    goEditProject() {
      this.$router.push(`/subscription/projects/${this.projectId}/edit/`)
    },
    openGitlab() {
      if (this.project.gitlab_url) {
        window.open(this.project.gitlab_url, '_blank', 'noopener')
      }
    },
    deleteSubscription(row) {
      const confirmDelete = async () => {
        try {
          await del(`/api/subscriptions/${row.id}/`)
          this.$bkMessage({ theme: 'success', message: '订阅已删除' })
          this.loadProject()
        } catch (error) {
          this.$bkMessage({ theme: 'error', message: error.message || '删除失败' })
        }
      }

      if (this.$bkInfo) {
        this.$bkInfo({
          title: '确认删除',
          subTitle: `确定删除订阅路径 ${row.path} 吗？`,
          confirmFn: confirmDelete
        })
      } else if (window.confirm(`确定删除订阅路径 ${row.path} 吗？`)) {
        confirmDelete()
      }
    },
    formatDate(value) {
      if (!value) {
        return '--'
      }
      return new Date(value).toLocaleString('zh-CN', { hour12: false })
    }
  }
}
</script>
