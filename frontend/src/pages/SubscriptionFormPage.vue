<template>
  <div class="two-column-grid" v-bkloading="{ isLoading: loading }">
    <section class="summary-card">
      <h3>GitLab 文件树</h3>
      <div class="toolbar">
        <div class="toolbar__grow">
          <bk-select v-model="selectedBranch" searchable @change="loadTree">
            <bk-option v-for="branch in branches" :key="branch.name" :id="branch.name" :name="branch.name" />
          </bk-select>
        </div>
        <bk-button @click="loadTree">刷新树</bk-button>
      </div>
      <div v-if="fileTree.length" class="file-tree">
        <button
          v-for="item in fileTree"
          :key="`${item.type}-${item.path}`"
          class="file-tree__item"
          :class="{ 'is-active': selectedPath === normalizePath(item) }"
          type="button"
          @click="applyTreeItem(item)">
          <span>{{ item.type === 'tree' ? '📁' : '📄' }} {{ normalizePath(item) }}</span>
          <span class="file-tree__type">{{ item.type === 'tree' ? '目录' : '文件' }}</span>
        </button>
      </div>
      <div v-else class="file-tree-empty">未加载到文件树，可手工录入路径。</div>
    </section>

    <section class="page-card">
      <div class="page-head">
        <div>
          <h2 class="page-title">新增订阅</h2>
          <p class="page-subtitle">为 {{ project.name || '当前项目' }} 配置目录或文件的变更订阅。</p>
        </div>
        <bk-button @click="$router.push(`/subscription/projects/${projectId}/`)">返回项目</bk-button>
      </div>

      <bk-alert type="info" title="路径规则" sub-title="目录订阅建议以 / 结尾，文件订阅填写准确的仓库相对路径。" />

      <bk-form class="form-grid form-grid--single" :label-width="120">
        <bk-form-item label="项目名称">
          <bk-input :value="project.name" disabled />
        </bk-form-item>
        <bk-form-item label="目标分支" required>
          <bk-input v-model.trim="form.branch" placeholder="例如 main" />
        </bk-form-item>
        <bk-form-item label="路径类型" required>
          <bk-select v-model="form.path_type">
            <bk-option id="directory" name="目录" />
            <bk-option id="file" name="文件" />
          </bk-select>
        </bk-form-item>
        <bk-form-item label="订阅路径" required>
          <bk-input v-model.trim="form.path" placeholder="例如 src/ 或 src/main.py" />
        </bk-form-item>
      </bk-form>

      <div class="form-actions">
        <bk-button theme="primary" :loading="submitting" @click="submit">保存订阅</bk-button>
        <bk-button @click="$router.push(`/subscription/projects/${projectId}/`)">取消</bk-button>
      </div>
    </section>
  </div>
</template>

<script>
import { get, post } from '../services/api'

export default {
  name: 'SubscriptionFormPage',
  props: {
    projectId: {
      type: [String, Number],
      required: true
    }
  },
  data() {
    return {
      loading: false,
      submitting: false,
      project: {},
      branches: [],
      fileTree: [],
      selectedBranch: '',
      selectedPath: '',
      form: {
        path: '',
        path_type: 'directory',
        branch: ''
      }
    }
  },
  created() {
    this.bootstrap()
  },
  methods: {
    async bootstrap() {
      this.loading = true
      try {
        const result = await get(`/api/projects/${this.projectId}/`)
        this.project = result.project || {}
        this.form.branch = this.project.default_branch || 'main'
        this.selectedBranch = this.form.branch
        this.branches = await get(`/api/projects/${this.projectId}/branches/`)
        await this.loadTree()
      } catch (error) {
        this.$bkMessage({ theme: 'error', message: error.message || '订阅页面初始化失败' })
      } finally {
        this.loading = false
      }
    },
    async loadTree() {
      const branch = this.selectedBranch || this.form.branch || this.project.default_branch || 'main'
      this.selectedBranch = branch
      this.form.branch = branch

      try {
        this.fileTree = await get(`/api/projects/${this.projectId}/tree/`, { branch })
      } catch (error) {
        this.fileTree = []
        this.$bkMessage({ theme: 'warning', message: error.message || '文件树加载失败，请手工录入路径' })
      }
    },
    normalizePath(item) {
      if (!item) {
        return ''
      }
      return item.type === 'tree' ? `${item.path}/` : item.path
    },
    applyTreeItem(item) {
      const normalized = this.normalizePath(item)
      this.selectedPath = normalized
      this.form.path = normalized
      this.form.path_type = item.type === 'tree' ? 'directory' : 'file'
    },
    validate() {
      if (!this.form.branch) {
        this.$bkMessage({ theme: 'error', message: '目标分支不能为空' })
        return false
      }
      if (!this.form.path) {
        this.$bkMessage({ theme: 'error', message: '订阅路径不能为空' })
        return false
      }
      return true
    },
    async submit() {
      if (!this.validate()) {
        return
      }

      this.submitting = true
      try {
        await post('/api/subscriptions/', {
          project: Number(this.projectId),
          path: this.form.path,
          path_type: this.form.path_type,
          branch: this.form.branch
        })
        this.$bkMessage({ theme: 'success', message: '订阅创建成功' })
        this.$router.push(`/subscription/projects/${this.projectId}/`)
      } catch (error) {
        this.$bkMessage({ theme: 'error', message: error.message || '订阅创建失败' })
      } finally {
        this.submitting = false
      }
    }
  }
}
</script>
