<template>
  <section class="page-card" v-bkloading="{ isLoading: loading }">
    <div class="page-head">
      <div>
        <h2 class="page-title">我的订阅</h2>
        <p class="page-subtitle">集中查看所有目录/文件订阅，并支持快速删除。</p>
      </div>
      <bk-button theme="primary" @click="$router.push('/subscription/projects/')">去新增订阅</bk-button>
    </div>

    <div class="toolbar">
      <div class="toolbar__grow">
        <bk-input v-model.trim="keyword" clearable placeholder="按项目、路径或分支筛选" />
      </div>
      <bk-button @click="loadSubscriptions">刷新</bk-button>
    </div>

    <bk-table :data="pagedSubscriptions" size="small" outer-border>
      <bk-table-column label="项目" min-width="180">
        <template slot-scope="{ row }">
          <bk-button text theme="primary" @click="$router.push(`/subscription/projects/${row.project}/`)">{{ row.project_name }}</bk-button>
        </template>
      </bk-table-column>
      <bk-table-column prop="path" label="订阅路径" min-width="240" />
      <bk-table-column label="类型" width="120">
        <template slot-scope="{ row }">{{ row.path_type === 'directory' ? '目录' : '文件' }}</template>
      </bk-table-column>
      <bk-table-column prop="branch" label="目标分支" width="140" />
      <bk-table-column prop="enterprise_username" label="通知用户名" width="140" />
      <bk-table-column label="创建时间" width="180">
        <template slot-scope="{ row }">{{ formatDate(row.created_at) }}</template>
      </bk-table-column>
      <bk-table-column label="操作" width="120" fixed="right">
        <template slot-scope="{ row }">
          <bk-button text theme="danger" @click="deleteSubscription(row)">删除</bk-button>
        </template>
      </bk-table-column>
    </bk-table>

    <div v-if="!loading && !filteredSubscriptions.length" class="empty-state">还没有任何订阅记录。</div>

    <bk-pagination
      v-if="filteredSubscriptions.length"
      :current.sync="pagination.current"
      :count="filteredSubscriptions.length"
      :limit.sync="pagination.limit"
      :limit-list="[10, 20, 50]"
      align="right"
      @change="handlePageChange"
      @limit-change="handleLimitChange" />
  </section>
</template>

<script>
import { del, get } from '../services/api'

export default {
  name: 'SubscriptionListPage',
  data() {
    return {
      loading: false,
      keyword: '',
      subscriptions: [],
      pagination: {
        current: 1,
        limit: 10
      }
    }
  },
  computed: {
    filteredSubscriptions() {
      const keyword = this.keyword.toLowerCase()
      if (!keyword) {
        return this.subscriptions
      }
      return this.subscriptions.filter((item) => {
        return [item.project_name, item.path, item.branch, item.enterprise_username]
          .filter(Boolean)
          .some((field) => String(field).toLowerCase().includes(keyword))
      })
    },
    pagedSubscriptions() {
      const start = (this.pagination.current - 1) * this.pagination.limit
      return this.filteredSubscriptions.slice(start, start + this.pagination.limit)
    }
  },
  watch: {
    keyword() {
      this.pagination.current = 1
    }
  },
  created() {
    this.loadSubscriptions()
  },
  methods: {
    async loadSubscriptions() {
      this.loading = true
      try {
        this.subscriptions = await get('/api/subscriptions/')
      } catch (error) {
        this.$bkMessage({ theme: 'error', message: error.message || '订阅列表加载失败' })
      } finally {
        this.loading = false
      }
    },
    deleteSubscription(row) {
      const confirmDelete = async () => {
        try {
          await del(`/api/subscriptions/${row.id}/`)
          this.$bkMessage({ theme: 'success', message: '订阅已删除' })
          this.loadSubscriptions()
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
