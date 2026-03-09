<template>
  <section class="page-card" v-bkloading="{ isLoading: loading }">
    <div class="page-head">
      <div>
        <h2 class="page-title">{{ pageTitle }}</h2>
        <p class="page-subtitle">前端直接调用 API 创建或更新 GitLab 项目配置。</p>
      </div>
      <bk-button @click="$router.push('/subscription/projects/')">返回项目列表</bk-button>
    </div>

    <bk-alert type="info" title="说明" sub-title="访问令牌需要具备读取仓库树与分支信息的权限。编辑时仍建议重新输入一次令牌，方便校验连接。" />

    <bk-form class="form-grid form-grid--single" :label-width="140">
      <bk-form-item label="项目名称" required>
        <bk-input v-model.trim="form.name" placeholder="请输入项目名称" />
      </bk-form-item>
      <bk-form-item label="项目描述">
        <bk-input v-model="form.description" type="textarea" :rows="4" placeholder="可选，补充项目用途说明" />
      </bk-form-item>
      <bk-form-item label="GitLab 地址" required>
        <bk-input v-model.trim="form.gitlab_url" placeholder="https://gitlab.example.com" />
      </bk-form-item>
      <bk-form-item label="GitLab 项目 ID" required>
        <bk-input v-model.trim="form.gitlab_project_id" type="number" placeholder="例如 1024" />
      </bk-form-item>
      <bk-form-item label="访问令牌" required>
        <bk-input v-model.trim="form.gitlab_token" type="password" placeholder="请输入访问令牌" />
      </bk-form-item>
      <bk-form-item label="默认分支" required>
        <bk-input v-model.trim="form.default_branch" placeholder="main" />
      </bk-form-item>
      <bk-form-item label="启用状态">
        <bk-switcher v-model="form.is_active" />
      </bk-form-item>
    </bk-form>

    <div class="form-actions">
      <bk-button theme="primary" :loading="submitting" @click="submit">保存</bk-button>
      <bk-button @click="$router.push('/subscription/projects/')">取消</bk-button>
    </div>
  </section>
</template>

<script>
import { get, post, put } from '../services/api'

export default {
  name: 'ProjectFormPage',
  props: {
    mode: {
      type: String,
      default: 'create'
    },
    projectId: {
      type: [String, Number],
      default: ''
    }
  },
  data() {
    return {
      loading: false,
      submitting: false,
      form: {
        name: '',
        description: '',
        gitlab_url: '',
        gitlab_project_id: '',
        gitlab_token: '',
        default_branch: 'main',
        is_active: true
      }
    }
  },
  computed: {
    pageTitle() {
      return this.mode === 'edit' ? '编辑 GitLab 项目' : '新增 GitLab 项目'
    }
  },
  created() {
    if (this.mode === 'edit' && this.projectId) {
      this.loadProject()
    }
  },
  methods: {
    async loadProject() {
      this.loading = true
      try {
        const result = await get(`/api/projects/${this.projectId}/`)
        const project = result.project || {}
        this.form = {
          ...this.form,
          ...project,
          gitlab_token: ''
        }
      } catch (error) {
        this.$bkMessage({ theme: 'error', message: error.message || '项目详情加载失败' })
      } finally {
        this.loading = false
      }
    },
    validate() {
      const requiredFields = [
        ['name', '项目名称'],
        ['gitlab_url', 'GitLab 地址'],
        ['gitlab_project_id', 'GitLab 项目 ID'],
        ['gitlab_token', '访问令牌'],
        ['default_branch', '默认分支']
      ]

      for (const [field, label] of requiredFields) {
        if (!this.form[field]) {
          this.$bkMessage({ theme: 'error', message: `${label}不能为空` })
          return false
        }
      }
      return true
    },
    async submit() {
      if (!this.validate()) {
        return
      }

      this.submitting = true
      try {
        const payload = {
          ...this.form,
          gitlab_project_id: Number(this.form.gitlab_project_id)
        }
        if (this.mode === 'edit') {
          await put(`/api/projects/${this.projectId}/`, payload)
          this.$bkMessage({ theme: 'success', message: '项目更新成功' })
        } else {
          await post('/api/projects/', payload)
          this.$bkMessage({ theme: 'success', message: '项目创建成功' })
        }
        this.$router.push('/subscription/projects/')
      } catch (error) {
        this.$bkMessage({ theme: 'error', message: error.message || '保存失败' })
      } finally {
        this.submitting = false
      }
    }
  }
}
</script>
