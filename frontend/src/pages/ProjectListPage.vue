<template>
  <section class="page-card" v-bkloading="{ isLoading: loading }">
    <div class="page-head">
      <div>
        <h2 class="page-title">GitLab 项目列表</h2>
        <p class="page-subtitle">查看项目接入情况，并进入订阅详情页维护规则。</p>
      </div>
      <bk-button v-if="canManage" theme="primary" icon="plus" @click="$router.push('/subscription/projects/create/')">
        新增项目
      </bk-button>
    </div>

    <div class="toolbar">
      <div class="toolbar__grow">
        <bk-input v-model.trim="keyword" clearable placeholder="按项目名、GitLab 地址或分支过滤" />
      </div>
      <bk-button @click="loadProjects">刷新</bk-button>
    </div>

    <bk-table :data="pagedProjects" size="small" outer-border>
      <bk-table-column label="项目" min-width="220">
        <template slot-scope="{ row }">
          <strong>{{ row.name }}</strong>
          <div class="inline-meta">{{ row.description || '暂无描述' }}</div>
        </template>
      </bk-table-column>
      <bk-table-column label="GitLab" min-width="220">
        <template slot-scope="{ row }">
          <a :href="row.gitlab_url" target="_blank" rel="noopener noreferrer">{{ row.gitlab_url }}</a>
          <div class="inline-meta">项目 ID：{{ row.gitlab_project_id }}</div>
        </template>
      </bk-table-column>
      <bk-table-column prop="default_branch" label="默认分支" width="120" />
      <bk-table-column label="订阅数" width="120">
        <template slot-scope="{ row }">
          {{ row.subscription_count }} / 我关注 {{ row.user_sub_count || 0 }}
        </template>
      </bk-table-column>
      <bk-table-column label="更新时间" width="160">
        <template slot-scope="{ row }">{{ formatDate(row.updated_at) }}</template>
      </bk-table-column>
      <bk-table-column label="操作" width="170" fixed="right">
        <template slot-scope="{ row }">
          <bk-button text theme="primary" @click="openDetail(row.id)">订阅</bk-button>
          <bk-button v-if="canManage" text theme="primary" @click="editProject(row.id)">编辑</bk-button>
        </template>
      </bk-table-column>
    </bk-table>

    <div v-if="!loading && !filteredProjects.length" class="empty-state">没有匹配的项目。</div>

    <bk-pagination
      v-if="filteredProjects.length"
      :current.sync="pagination.current"
      :count="filteredProjects.length"
      :limit.sync="pagination.limit"
      :limit-list="[10, 20, 50]"
      align="right"
      @change="handlePageChange"
      @limit-change="handleLimitChange" />
  </section>
</template>

<script>
import { get } from '../services/api'

export default {
  name: 'ProjectListPage',
  data() {
    return {
      loading: false,
      canManage: false,
      keyword: '',
      projects: [],
      pagination: {
        current: 1,
        limit: 10
      }
    }
  },
  computed: {
    filteredProjects() {
      const keyword = this.keyword.toLowerCase()
      if (!keyword) {
        return this.projects
      }
      return this.projects.filter((item) => {
        return [item.name, item.description, item.gitlab_url, item.default_branch]
          .filter(Boolean)
          .some((field) => String(field).toLowerCase().includes(keyword))
      })
    },
    pagedProjects() {
      const start = (this.pagination.current - 1) * this.pagination.limit
      return this.filteredProjects.slice(start, start + this.pagination.limit)
    }
  },
  watch: {
    keyword() {
      this.pagination.current = 1
    }
  },
  created() {
    this.loadProjects()
  },
  methods: {
    async loadProjects() {
      this.loading = true
      try {
        const result = await get('/api/projects/')
        this.projects = result.projects || []
        this.canManage = Boolean(result.can_manage)
      } catch (error) {
        this.$bkMessage({ theme: 'error', message: error.message || '项目列表加载失败' })
      } finally {
        this.loading = false
      }
    },
    openDetail(projectId) {
      this.$router.push(`/subscription/projects/${projectId}/`)
    },
    editProject(projectId) {
      this.$router.push(`/subscription/projects/${projectId}/edit/`)
    },
    handlePageChange(page) {
      this.pagination.current = page
    },
    handleLimitChange(limit) {
      this.pagination.limit = limit
      this.pagination.current = 1
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
